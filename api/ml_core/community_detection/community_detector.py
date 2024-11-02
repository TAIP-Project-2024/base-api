class CommunityDetector:
    """
    CommunityDetector serves as a Facade for various community detection algorithms,
    providing a simplified interface to detect communities within a graph.
    """

    def __init__(self):
        self.algorithm = None  # Selected community detection algorithm

    def set_algorithm(self, algorithm):
        """
        Sets the community detection algorithm to use.

        :param algorithm: An instance of a specific community detection algorithm (e.g., GirvanNewman, Louvain)
        """
        self.algorithm = algorithm

    def detect_communities(self, graph):
        """
        Detects communities within the provided graph using the selected algorithm.

        :param graph: Graph to analyze for community detection
        :return: List of communities
        """
        if not self.algorithm:
            raise ValueError("No community detection algorithm has been set.")
        return self.algorithm.detect_communities(graph)
