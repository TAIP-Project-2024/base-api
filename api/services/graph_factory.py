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
    def topics_similarity_based_graph(name, topics, similarities, t = 0):
        """
        Args:
            name: name for the graph
            similarities: a similarity matrix
            t: similarity threshold
            returns a list of lists of indices representing communities,
        """
        n = len(similarities[0])
        hairball = nx.Graph()

        edges_tuples = [
            (i, j, similarities[i][j])
            for i in range(n)
            for j in range(i+1, n)
            if similarities[i][j] > t
        ]
        hairball.add_weighted_edges_from(edges_tuples)
        nx.set_node_attributes(hairball, topics)
        partitions = nx.community.louvain_communities(hairball)

        if len(partitions) > 10:
            raise Exception("provide more colors :)")

        for i, partition in enumerate(partitions):
            for node in partition:
                hairball.nodes[node]['color'] = COMMUNITY_COLORS[i]
                hairball.nodes[node]['community'] = i

        graph = NetworkxGraphImpl(name, hairball)

        return graph


similarities = random_matrix = [
    [random.randint(1, 10)
     for _ in range(100)]
    for _ in range(100)]

topics = {}
for i in range(100):
    topics[i] = {'title':f'topic {i}', 'url':f'https://networkx.org/documentation/stable/index.html'}
print(topics)
# g = GraphFactory.topics_similarity_based_graph('cool_graph', topics, similarities)
# g.save()
