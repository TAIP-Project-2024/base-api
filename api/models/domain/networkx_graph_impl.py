import os

import networkx as nx

from api.models.domain.graph import Graph

"""
    Example of 2 concrete implementations for a graph framework object
"""

class NetworkxDiGraphImpl(Graph):

    def __init__(self, name, graph = None):
        super().__init__(name)
        self.saved_locally = False
        if graph is not None:
            self.graph = graph
        else:
            if not os.path.isfile(self.graphml_file):
                self.graph = nx.Graph()
            else:
                self.graph = nx.read_graphml(self.graphml_file)
                self.saved_locally = True

        #id will be set when added to cloud
        self.id = None

    def save(self):
        nx.write_graphml(self.graph, self.graphml_file)


class NetworkxGraphImpl(Graph):

    def __init__(self, name, graph = None):
        super().__init__(name)
        self.saved_locally = False
        if graph is not None:
            self.graph = graph
        else:
            if not os.path.isfile(self.graphml_file):
                self.graph = nx.Graph()
            else:
                self.graph = nx.read_graphml(self.graphml_file)
                self.saved_locally = True

        #id will be set when added to cloud
        self.id = None

    def save(self):
        nx.write_graphml(self.graph, self.graphml_file)

    def clear_graph(self):
        self.graph = nx.Graph()
