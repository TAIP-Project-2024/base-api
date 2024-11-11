from abc import ABC, abstractmethod


class CommunityDetectionAlgorithm(ABC):
    """
    CommunityDetectionAlgorithm defines the Strategy interface for community detection algorithms.
    Concrete algorithms implementing this interface will define the `detect_communities` method.
    Implements the Strategy Pattern to allow flexible community detection approaches.
    """

    @abstractmethod
    def detect_communities(self, graph):
        """
        Detects communities within the provided graph.

        :param graph: The graph to analyze for community structure
        :return: List of detected communities
        """
        pass


class GirvanNewman(CommunityDetectionAlgorithm):
    """
    GirvanNewman implements a specific community detection algorithm (Girvan-Newman),
    used for identifying communities by iteratively removing edges with the highest betweenness.
    Extends CommunityDetectionAlgorithm as a concrete strategy.
    """

    def detect_communities(self, graph):
        """
        Detects communities using the Girvan-Newman algorithm.

        :param graph: The graph to analyze
        :return: List of detected communities
        """
        # Implementation for Girvan-Newman community detection
        pass


class Louvain(CommunityDetectionAlgorithm):
    """
    Louvain implements the Louvain method for community detection,
    which optimizes modularity by grouping nodes into communities.
    Extends CommunityDetectionAlgorithm as a concrete strategy.
    """

    def detect_communities(self, graph):
        """
        Detects communities using the Louvain algorithm.

        :param graph: The graph to analyze
        :return: List of detected communities
        """
        # Implementation for Louvain community detection
        pass
