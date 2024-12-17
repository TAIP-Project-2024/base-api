import random

import networkx as nx
from django.template.context_processors import static

from api.models.domain.networkx_graph_impl import NetworkxDiGraphImpl, NetworkxGraphImpl
from api.services.general.graph_service import GraphService

COMMUNITY_COLORS = [
    "#007BA7",
    "#7851A9",
    "#9400D3",
    "#6F00FF",
    "#00FFFF",
    "#FFBF00",
    "#CC5500",
    "#FFFFF0",
    "#008080",
    "#DAA520"
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
                    if similarities[line[0]][value] > t:
                            edges_tuples.append((line[0], value, similarities[line[0]][value]))
                except KeyError as ke:
                    print(1)
                    print(ke)
                    continue

        hairball.add_weighted_edges_from(edges_tuples)
        nx.set_node_attributes(hairball, posts)
        partitions = nx.community.louvain_communities(hairball)

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
            graph.nodes[group]['size']=n[group]+30

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