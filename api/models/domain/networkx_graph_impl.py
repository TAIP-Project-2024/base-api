import networkx as nx

from api.models.domain.graph import Graph
from api.models.domain.graph_drawing import GraphDrawing
from api.services.layouts.simple_nx_drawing import SimpleNxDrawing

"""
    Example of a concrete implementation for a graph framework object
"""
class NetworkxGraphImpl(Graph):

    def __init__(self, file):
        self.graph = nx.read_graphml(file)

    def save(self, file):
        nx.write_graphml(self.graph, file)



#demo, can run
g = NetworkxGraphImpl("../../../resources/graphs/marvel.graphml")
d = GraphDrawing(g)
d.draw(SimpleNxDrawing())
# open the html generated in resources/drawings.