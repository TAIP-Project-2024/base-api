import os

import networkx as nx

from api.models.domain.graph import Graph

"""
    Example of a concrete implementation for a graph framework object
"""

class NetworkxDiGraphImpl(Graph):

    def __init__(self, name, graph = None):
        super().__init__(name)
        if not os.path.isfile(self.graphml_file):
            self.saved_locally = False
            if graph is None:
                self.graph = nx.DiGraph()
            else:
                self.graph = graph
        else:
            self.graph = nx.read_graphml(self.graphml_file)
            self.saved_locally = True

        #id will be set when added to cloud
        self.id = None

    def save(self):
        nx.write_graphml(self.graph, self.graphml_file)

# g = NetworkxDiGraphImpl('marvel')
# print(g.saved_locally)
# print(g.graphml_file)
