import random
from pydoc_data.topics import topics

import networkx as nx
from pyvis.network import Network

from api.models.domain.graph_drawing import GraphDrawing
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
        n = len(posts)
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


node_ids = ['mtr', 'hpa', 'vip', 'uem', 'pbf', 'rwc', 'dtk', 'hdw', 'wuw', 'aem',
             'ecm', 'rhv', 'pbs', 'bwa', 'yel', 'pwf', 'nbm', 'uxd', 'wis', 'zmv',
             'otw', 'puk', 'sjr', 'lvh', 'vwv', 'jkt', 'flu', 'ghi', 'qui', 'wwn',
             'tpb', 'irt', 'oge', 'amd', 'vfr', 'txz', 'ahc', 'cyt', 'fwl', 'pkr',
             'ivk', 'dfj', 'jnk', 'cxw', 'mqm', 'wqr', 'sqp', 'iwb', 'gqz', 'vso',
             'zyo', 'cao', 'xal', 'kgk', 'mua', 'vzy', 'rlt', 'mze', 'oxw', 'iur',
             'ypi', 'cvk', 'zwb', 'qta', 'wrr', 'zgp', 'rfu', 'ipe', 'fid', 'rkk',
             'xbi', 'hst', 'dfc', 'wai', 'edf', 'kzn', 'rhx', 'wug', 'wsl', 'aau',
             'ddy', 'jqh', 'cln', 'okb', 'prd', 'bui', 'lqw', 'ork', 'qad', 'rct',
             'lje', 'rwu', 'mrw', 'nvj', 'muh', 'tin', 'xmg', 'ddg', 'tgj', 'zlq']

similarities = {id_: {id_: random.randint(1, 10) for id_ in node_ids} for id_ in node_ids}
topics = {}
for i in range(100):
    id = node_ids[i]
    topics[id] = {'title':f'topic {id}', 'url':f'https://networkx.org/documentation/stable/index.html'}
print(topics)
g = GraphFactory.topics_similarity_based_graph('cool_graph', topics, similarities)
g.save()
