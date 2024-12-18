import os
import random

import networkx as nx
from django.template.context_processors import static
from dotenv import load_dotenv
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer, util

from api.models.domain.networkx_graph_impl import NetworkxDiGraphImpl, NetworkxGraphImpl
from api.repositories.general.graph_drawing_repository import DrawingRepository
from api.repositories.general.posts_repository import PostsRepository
from api.services.general.graph_service import GraphService
from api.services.layouts.community_stars import CommunityStars

COMMUNITY_COLORS = [
    "#3C3ABF",
    "#86159A",
    "#004F8E",
    "#8F2C2E",
    "#980000",
    "#364A80",
    "#185B1B",
    "#3A5718",
    "#9C1341",
    "#065A4F"
]

class GraphFactory:

    @staticmethod
    def random_graph(n):
        graph = NetworkxDiGraphImpl(f"random{n}barabasi", nx.barabasi_albert_graph(n, int(n/1.5)))
        return graph

    @staticmethod
    def topics_similarity_based_graph(name, posts, similarities, t = 0):
        """
        Args:
            name: name for the graph
            similarities: a similarity matrix
            t: similarity threshold
            returns a list of lists of indices representing communities,
        """
        hairball = nx.Graph()

        edges_tuples = []
        for line in similarities.items():
            for value in line[1]:
                try:
                    if similarities[line[0]][value] > t and value != line[0]:
                            edges_tuples.append((line[0], value, similarities[line[0]][value]))
                except KeyError as ke:
                    print(1)
                    print(ke)
                    continue

        hairball.add_weighted_edges_from(edges_tuples)
        nx.set_node_attributes(hairball, posts)
        partitions = nx.community.louvain_communities(hairball)
        print(f'detected {len(partitions)} partitions')
        if len(partitions) > 10:
            raise Exception("provide more colors :)")

        for i, partition in enumerate(partitions):
            for node in partition:
                hairball.nodes[node]['color'] = COMMUNITY_COLORS[i]
                hairball.nodes[node]['community'] = i

        graph = NetworkxGraphImpl(name, hairball)

        return graph
    @staticmethod
    def create_comments_graph(graph_name, post_text, comments, base_size = 15):
        """
        Args
        : post {text, url}
        : comments an array of objects that have an id,
        a body and a sentiment rank
        {id, title, sentiment, group(0,1,2)}
        """
        groups = ["group_negative", "group_neutral", "group_positive"]
        colors = ["red", "gray", "green"]
        graph = nx.Graph()
        graph.add_node("post", title=post_text, url="url", size = 25, color = "yellow")
        graph.add_node("group_neutral", label="Neutral", color="gray", size = base_size)
        graph.add_node("group_negative", label="Negative", color="red", size = base_size)
        graph.add_node("group_positive", label="Positive", color="green", size = base_size)
        graph.add_edges_from([("post", "group_neutral"), ("post", "group_positive"), ("post", "group_negative")])
        n = {}

        for group in groups:
            n[group] = 0

        print([e["sentiment"] for e in comments])
        for entry in comments:
            group = groups[round(entry["sentiment"])]
            color = colors[entry["sentiment"]]
            label = "score " + str(entry["score"])
            print(color)
            graph.add_node(entry["_id"],
                           title=entry["text"],
                           label = label,
                           color=color,
                           group=group,
                           size=base_size,
                           hidden=True)

            graph.add_edge(group, entry["_id"])
            n[group] += 1

        for group in groups:
            try:
                graph.nodes[group]['size']=n[group]+30
            except:
                pass # means no such members
        return NetworkxGraphImpl(graph_name, graph)


# node_ids = ['mtr', 'hpa', 'vip', 'uem', 'pbf', 'rwc', 'dtk', 'hdw', 'wuw', 'aem',
#              'ecm', 'rhv', 'pbs', 'bwa', 'yel', 'pwf', 'nbm', 'uxd', 'wis', 'zmv',
#              'otw', 'puk', 'sjr', 'lvh', 'vwv', 'jkt', 'flu', 'ghi', 'qui', 'wwn',
#              'tpb', 'irt', 'oge', 'amd', 'vfr', 'txz', 'ahc', 'cyt', 'fwl', 'pkr',
#              'ivk', 'dfj', 'jnk', 'cxw', 'mqm', 'wqr', 'sqp', 'iwb', 'gqz', 'vso',
#              'zyo', 'cao', 'xal', 'kgk', 'mua', 'vzy', 'rlt', 'mze', 'oxw', 'iur',
#              'ypi', 'cvk', 'zwb', 'qta', 'wrr', 'zgp', 'rfu', 'ipe', 'fid', 'rkk',
#              'xbi', 'hst', 'dfc', 'wai', 'edf', 'kzn', 'rhx', 'wug', 'wsl', 'aau',
#              'ddy', 'jqh', 'cln', 'okb', 'prd', 'bui', 'lqw', 'ork', 'qad', 'rct',
#              'lje', 'rwu', 'mrw', 'nvj', 'muh', 'tin', 'xmg', 'ddg', 'tgj', 'zlq']
#
# similarities = {id_: {id_: random.randint(1, 10) for id_ in node_ids} for id_ in node_ids}
# topics = {}
# for i in range(100):
#     id = node_ids[i]
#     topics[id] = {'title':f'topic {id}', 'url':f'https://networkx.org/documentation/stable/index.html'}
# print(topics)
# g = GraphFactory.topics_similarity_based_graph('cool_graph', topics, similarities)
# g.save()
# GraphService().save_graph(NetworkxGraphImpl("cool_graph"), False)


# load_dotenv('.env')
# DATABASE_NAME = os.environ.get("MONGO_DB_NAME")
# MONGO_URI = os.environ.get("MONGO_URI")
# client = MongoClient(MONGO_URI)
# db = client[DATABASE_NAME]
# reddit_posts = PostsRepository(db).get_all()
#
# posts = {}
#
# post_ids = []
#
# for reddit_post in reddit_posts:
#     post_ids.append(reddit_post.id())
#     posts[reddit_post.id()] = {'title': reddit_post.title, 'url': 'reddit.com/r/politics'}
#
# print(posts)
#
# model = SentenceTransformer('all-MiniLM-L6-v2')
#
# posts_texts = [posts[post_id]['title'] for post_id in post_ids]
#
# embeddings = model.encode(posts_texts, batch_size=16, convert_to_tensor=True)
# sim = util.cos_sim(embeddings, embeddings)
#
# similarities = {i: {j: sim[post_ids.index(i)][post_ids.index(j)].item()*10 for j in post_ids} for i in post_ids}
#
# print(similarities)
#
# g = GraphFactory.topics_similarity_based_graph('latest_posts3', posts, similarities)
# g.save()
# GraphService().save_graph(NetworkxGraphImpl('latest_posts3'), False)
#
# GraphDrawingService().save_graph_drawing('latest_posts', GraphDrawingService().generate_drawing(CommunityStars(), NetworkxGraphImpl('latest_posts'), 'lates_posts.html'), False)
#


