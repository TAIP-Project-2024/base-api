class GraphBuilder:
    """
    GraphBuilder assists in constructing a graph structure to represent networks for community detection.
    This class follows a simple Builder Pattern to incrementally construct a network graph.
    """

    def __init__(self):
        """
        Initializes the GraphBuilder with an empty graph structure.
        """
        self.graph = {}  # Dictionary to hold the graph structure

    def add_edge(self, node_a, node_b):
        """
        Adds an edge between two nodes, creating the nodes if they do not exist in the graph.

        :param node_a: First node in the edge
        :param node_b: Second node in the edge
        """
        if node_a not in self.graph:
            self.graph[node_a] = []
        self.graph[node_a].append(node_b)

    def get_graph(self):
        """
        Returns the constructed graph representation.

        :return: The constructed graph as a dictionary of nodes and edges
        """
        return self.graph
