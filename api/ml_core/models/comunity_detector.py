# community_detector.py

import networkx as nx
from community import community_louvain


class CommunityDetector:
    """Defines a community detection model using the Louvain method.
    Implements the Facade pattern to simplify the community detection process."""

    def __init__(self):
        """Initializes the CommunityDetector."""
        self.graph = nx.Graph()  # Initialize a graph

    def add_edges(self, edges):
        """
        Adds edges to the community detection graph.

        Args:
            edges: List of edges to add to the graph.
        """
        self.graph.add_edges_from(edges)  # Add edges to the graph

    def detect_communities(self):
        """Detects communities in the graph using the Louvain method."""
        partition = community_louvain.best_partition(self.graph)  # Detect communities
        return partition  # Return the community assignment for each node

    def visualize_communities(self, partition):
        """
        Visualizes the detected communities using a simple layout.

        Args:
            partition: The community assignment for each node.
        """
        import matplotlib.pyplot as plt

        # Visualize the communities
        pos = nx.spring_layout(self.graph)
        cmap = plt.get_cmap("Set1")
        for community_id in set(partition.values()):
            nodes = [node for node in partition.keys() if partition[node] == community_id]
            nx.draw_networkx_nodes(self.graph, pos, nodelist=nodes, node_color=cmap(community_id))
        nx.draw_networkx_edges(self.graph, pos, alpha=0.5)
        plt.show()
