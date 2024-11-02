from abc import ABC, abstractmethod


class CommunityDetectionAlgorithm(ABC):
    """
    CommunityDetectionAlgorithm defines the Strategy interface for community detection algorithms.
    Concrete algorithms will implement the `detect_communities` method.
    """

    @abstractmethod
    def detect_communities(self, graph):
        """
        Detects communities within the provided graph.

        :param graph: The graph to analyze
        :return: List of communities
        """
        pass


class GirvanNewman(CommunityDetectionAlgorithm):
    """
    GirvanNewman implements a specific community detection algorithm (Girvan-Newman),
    used for detecting communities by iteratively removing edges with the highest betweenness.
    """

    def detect_communities(self, graph):
        # Implementation for Girvan-Newman community detection
        pass


class Louvain(CommunityDetectionAlgorithm):
    """
    Louvain implements the Louvain method for community detection,
    which optimizes modularity by iteratively grouping nodes into communities.
    """

    def detect_communities(self, graph):
        # Implementation for Louvain community detection
        pass
