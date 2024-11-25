class CommunityDetector:
    """
    CommunityDetector serves as a Facade for various community detection algorithms,
    providing a simplified interface to detect communities within a graph.
    Uses the Facade Pattern to streamline community detection process.
    """

    def __init__(self):
        """
        Initializes the CommunityDetector with no algorithm set initially.
        """
        self.algorithm = None  # Selected community detection algorithm

    def set_algorithm(self, algorithm):
        """
        Sets the community detection algorithm to be used.

        :param algorithm: An instance of a specific community detection algorithm (e.g., GirvanNewman, Louvain)
        """
        self.algorithm = algorithm

    def detect_communities(self, graph):
        """
        Detects communities within the provided graph using the selected algorithm.
        Raises an error if no algorithm is set.

        :param graph: The graph to analyze for community structure
        :return: List of detected communities
        """
        if not self.algorithm:
            raise ValueError("No community detection algorithm has been set.")
        return self.algorithm.detect_communities(graph)
