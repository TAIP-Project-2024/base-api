import os
from abc import abstractmethod

from BaseAPI.settings import BASE_DIR

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
        self.name = name
        self.graphml_file = self.resolve_path(self.name)

    @abstractmethod
    def save(self):
        """
        save's a graph object using a framework's method
        e.g. graph = NewtworkX.write_graphml()

        will save locally with the possibility of being
        deleted when saved to cloud.
        """
        pass

    @abstractmethod
    def clear_graph(self):
        pass

    @staticmethod
    def resolve_path(name):
        return str(BASE_DIR / os.environ.get('LOCAL_GRAPHS_DIR') / (name + '.graphml'))
