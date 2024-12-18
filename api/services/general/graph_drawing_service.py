import os
from io import BytesIO

from torch.cuda import graph

from api.models.domain.graph_drawing import GraphDrawing
from api.models.domain.networkx_graph_impl import NetworkxGraphImpl
from api.repositories.general.comments_repository import CommentsRepository
from api.repositories.general.graph_drawing_repository import DrawingRepository
from api.repositories.general.graph_repository import GraphRepository
from api.services.general.graph_service import GraphService
from api.services.graph_factory import GraphFactory
from api.services.layouts.comments_drawing import CommentsDrawing
from api.services.layouts.community_stars import CommunityStars


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

    def create_or_retrieve_comments_drawing(self, post_id, post_text):
        drawing_name = f"{post_id}CommentsGraphDrawing"
        if self.check_exists(drawing_name):
            res = self.find_drawing_by_name(drawing_name)
            print("new graph")
            return res
        else:
            print("existing_graph")
            graph_name=f"{post_id}CommentsGraph"
            gs = GraphService()
            if gs.check_exists(graph_name):
                gs.fetch_graph_locally(graph_name)
                graph = NetworkxGraphImpl(graph_name)
            else:
                #build the graph
                with CommentsRepository() as c:
                    comments = c.get_comments_for_post(post_id)
                graph = GraphFactory.create_comments_graph(graph_name, post_text, comments)
                gs.save_graph(graph, False)
            gd = GraphDrawing(graph, drawing_name)
            gd.draw_as(CommentsDrawing(width = '100vw',
                                        height = '100vh',
                                        n = 800))
            self.save_graph_drawing(GraphDrawing(None, drawing_name), False)
            try:
                os.remove(graph.graphml_file)
            except:
                pass
            with open(gd.html_file, "rb") as f:
                return BytesIO(f.read())

#
#
# buffer  = GraphDrawingService().create_or_retrieve_comments_drawing("1hfkiuh", "some_post")
# print(type(buffer))

# GraphDrawingService().generate_drawing(CommunityStars("Politics"), NetworkxGraphImpl('latest_posts3'), 'LatestPosts')
# GraphDrawingService().save_graph_drawing(GraphDrawing(NetworkxGraphImpl('latest_posts3'), name="LatestPosts"), False)




