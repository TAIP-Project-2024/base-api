from abc import abstractmethod
import uuid

"""
    This class is a decorator over a framework
    specific object representing a graph.

    This is also an adapter between multiple frameworks.

"""


class Graph:

    @abstractmethod
    def __init__(self, file, name):
        """
        initializes a graph object using a framework's factory method
        e.g. graph = NewtworkX.read_graphml()
        @param file: path to a file of .graphml format.

        """
        pass

    @abstractmethod
    def save_graph(self, file):
        """
        save's a graph object using a framework's method
        e.g. graph = NewtworkX.write_graphml()

        @param file: path to a file of .graphml format.

        will save locally with the possibility of being
        deleted when saved to cloud.
        """
        pass