class GraphBuilder:
    def __init__(self):
        """
        Initializes the GraphBuilder.
        This class helps to construct graph structures for community detection.
        """
        self.graph = {}  # Dictionary to hold the graph structure

    def add_edge(self, node_a, node_b):
        """
        Adds an edge between two nodes in the graph.

        :param node_a: First node
        :param node_b: Second node
        """
        if node_a not in self.graph:
            self.graph[node_a] = []
        self.graph[node_a].append(node_b)

    def get_graph(self):
        """
        Returns the constructed graph.

        :return: Graph structure
        """
        return self.graph
