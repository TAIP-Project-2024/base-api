import networkx as nx

from api.models.domain.graph import Graph
from api.models.domain.graph_drawing import GraphDrawing
from api.services.layouts.simple_nx_drawing import SimpleNxDrawing

"""
    Example of a concrete implementation for a graph framework object
"""


class NetworkxDiGraphImpl(Graph):

    def __init__(self, file, name):
        #id will be set when added to cloud
        self.id = None
        self.name = name
        if file is None:
            self.graph = nx.DiGraph()
        else:
            self.graph = nx.read_graphml(file)
        self.graphml_file = file

    def save(self, file):
        nx.write_graphml(self.graph, file)

