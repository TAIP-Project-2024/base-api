import datetime
import os
from io import BytesIO
from datetime import datetime

from lxml.html.builder import FRAME
from sentence_transformers import SentenceTransformer, util
from torch.cuda import graph

from api.models.domain.graph_drawing import GraphDrawing
from api.models.domain.networkx_graph_impl import NetworkxGraphImpl
from api.repositories.general.comments_repository import CommentsRepository
from api.repositories.general.graph_drawing_repository import DrawingRepository
from api.services.general.graph_service import GraphService
from api.services.general.posts_service import PostsService
from api.services.graph_factory import GraphFactory
from api.services.layouts.comments_drawing import CommentsDrawing
from api.services.layouts.community_stars import CommunityStars
from api.services.layouts.design_config import ForceDirectedLouvain_kwargs, CommunityStars_kwargs, \
    post_similarity_graph_kwargs, comments_graph_kwargs, CommentsDrawing_kwargs, comments_graph_name_format, \
    comments_graph_drawing_name_format, posts_sim_graph_name_format, hairball_drawing_name_format, \
    community_drawing_name_format
from api.services.layouts.force_directed_louvain import ForceDirectedLouvain


class GraphDrawingService:
    def __init__(self):
        pass

    def generate_drawing(self, layout, graph, name):
        """
        Will try to apply the layout algorithm for the graph
        Will return false if it fails.
        """
        graph_drawing = GraphDrawing(graph, name)
        return graph_drawing.draw_as(layout)

    def generate_and_save_drawing(self, layout, graph, name):
        graph_drawing = GraphDrawing(graph, name)
        graph_drawing.draw_as(layout)
        self.save_graph_drawing(graph_drawing, False)

    def save_graph_drawing(self, graph_drawing, delete_local=False):
        #retrieve the local file
        if not graph_drawing.is_drawn:
            # todo exception
            print('not drawn')
            return

        with open(graph_drawing.html_file, "rb") as file_buffer:
            #save to cloud
            with DrawingRepository() as drawing_repository:
                drawing_repository.add(graph_drawing.name, file_buffer)
        if delete_local:
            os.remove(graph_drawing.html_file)

    def find_drawing_by_name(self, name):
        with DrawingRepository() as drawing_repository:
            file_buffer = drawing_repository.get(name)
        return file_buffer

    def delete_drawing(self, name):
        with DrawingRepository() as drawing_repository:
            return drawing_repository.delete(name)

    def fetch_drawing_locally(self, name):
        with DrawingRepository() as graph_drawing_repo:
            file_buffer = graph_drawing_repo.get(name)
            path = GraphDrawing.resolve_path(name)
            with open(path, 'wb') as file:
                # file.write(file_buffer.read())
                while True:
                    chunk = file_buffer.read(2048)
                    if not chunk:
                        break
                    file.write(chunk)

    def check_exists(self, name):
        with DrawingRepository() as dr:
            return dr.check_exists(name)

    def clear_comments_drawings_for_topic(self, topic):
        regex_pattern = '^post#[a-z0-9]{7}CommentsGraphDrawing'+f'\\[{topic}\\]'+'$'
        with DrawingRepository() as dr:
            comments_drawings = dr.find_by_regex(regex_pattern)
            ids = [d._id for d in comments_drawings]
            if (len(ids) > 0):
                dr.delete_from_list(ids)

    def delete_all_except(self, keep):
        """
        deletes all graphs drawings except those in the keep list
        """
        keep_set = set(keep)
        with DrawingRepository() as dr:
            all_drawings = dr.get_all_names()
            for name in all_drawings:
                if name not in keep_set:
                    dr.delete(name)

    def get_all_drawing_names(self):
        with DrawingRepository() as dr:
            return dr.get_all_names()

    def create_or_retrieve_comments_drawing(self, topic, post_id, post_text):
        """
        Given a post id,
            if a graph drawing representing the comments for the post exists in the db, returns it
            if such a drawing does not exist, creates it. If the underlying graph structure does not
            exist as well, creates it first. Else, retrieves it from te db.
        """
        drawing_name = comments_graph_drawing_name_format(post_id, topic)
        if self.check_exists(drawing_name):
            res = self.find_drawing_by_name(drawing_name)
            print("[SERVER LOG] existing comments graph drawing")
            return res
        else:
            print("[SERVER LOG] new comments graph")
            graph_name=comments_graph_name_format(post_id, topic)
            gs = GraphService()
            if gs.check_exists(graph_name):
                gs.fetch_graph_locally(graph_name)
                graph = NetworkxGraphImpl(graph_name)
            else:
                #build the graph
                with CommentsRepository() as c:
                    comments = c.get_comments_for_post(post_id)
                graph = GraphFactory.create_comments_graph(graph_name, post_text, comments, **comments_graph_kwargs)
                gs.save_graph(graph, False)
            gd = GraphDrawing(graph, drawing_name)
            gd.draw_as(CommentsDrawing(**CommentsDrawing_kwargs))
            self.save_graph_drawing(GraphDrawing(None, drawing_name), False)
            try:
                os.remove(graph.graphml_file)
            except:
                pass
            with open(gd.html_file, "rb") as f:
                return BytesIO(f.read())

    def process_topic(self, topic, clear_comments = True, clear_all = False):

        # retrieve comments and prepare input data
        reddit_posts = PostsService().get_topic_posts(topic)
        posts = {}
        post_texts = []
        post_ids = []
        for p in reddit_posts:
            post_ids.append(p["_id"])
            posts[p["_id"]] = {'title': p['title'], 'url': p['url'], 'label': " "}
            post_texts.append(p['title'])

        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = model.encode(post_texts, batch_size=16, convert_to_tensor=True)
        sim = util.cos_sim(embeddings, embeddings)
        similarities = {}

        for i, i_id in enumerate(post_ids):
            for j, j_id in enumerate(post_ids[i+1:], start = i + 1):
                similarity_i_j = sim[i][j].item() * 10
                if i_id not in similarities:
                    similarities[i_id] = {}
                similarities[i_id][j_id] = similarity_i_j

        # create the posts similarity graph with all the posts.
        timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        posts_sim_graph_name = posts_sim_graph_name_format(topic, timestamp)

        posts_sim_graph = GraphFactory.posts_similarity_based_graph(posts_sim_graph_name,
                                                                    posts,
                                                                    similarities,
                                                                    **post_similarity_graph_kwargs)
        posts_sim_graph.save()
        graph_service = GraphService()
        graph_service.save_graph(posts_sim_graph, False)

        #create and save the 2 drawings

        #create the hairball graph drawing
        hairball_drawing_name = hairball_drawing_name_format(topic, timestamp)
        hairball_layout = ForceDirectedLouvain(topic = topic, **ForceDirectedLouvain_kwargs)
        self.generate_and_save_drawing(hairball_layout, posts_sim_graph, hairball_drawing_name)

        #create the community stars
        community_drawing_name = community_drawing_name_format(topic, timestamp)
        community_stars_layout =  CommunityStars(topic = topic, **CommunityStars_kwargs)
        self.generate_and_save_drawing(community_stars_layout, posts_sim_graph, community_drawing_name)

        if clear_all:
            self.delete_all_except([hairball_drawing_name, community_drawing_name]) #drawings
            graph_service.delete_all_except([posts_sim_graph_name])
        elif clear_comments:
            self.clear_comments_drawings_for_topic(topic)
            graph_service.clear_comments_graphs_for_topic(topic)

