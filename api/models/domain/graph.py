import os
from abc import abstractmethod
import uuid

"""
    This class is a decorator over a framework
    specific object representing a graph.

    This is also an adapter between multiple frameworks.

"""


class Graph:

    @abstractmethod
    def __init__(self, name):
        """
        initializes a graph object using a framework's factory method
        e.g. graph = NewtworkX.read_graphml()
        """
        self.storage = '../../../' + os.environ.get('LOCAL_GRAPHS_DIR')
        self.graphml_file = self.storage + name + '.graphml'

    @abstractmethod
    def save_graph(self):
        """
        save's a graph object using a framework's method
        e.g. graph = NewtworkX.write_graphml()

        will save locally with the possibility of being
        deleted when saved to cloud.
        """
        pass