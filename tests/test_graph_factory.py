import unittest
from unittest.mock import patch
import random
import networkx as nx
from networkx.classes import Graph

from api.services.graph_factory import GraphFactory
from api.models.domain.networkx_graph_impl import NetworkxGraphImpl, NetworkxDiGraphImpl


class GraphFactoryTests(unittest.TestCase):

    @patch('api.services.graph_factory.NetworkxDiGraphImpl')
    @patch('networkx.barabasi_albert_graph')
    def test_random_graph(self, mock_barabasi_albert_graph, mock_graph_impl):
        # Setup mock graph
        n = 10
        mock_graph = nx.Graph()
        mock_barabasi_albert_graph.return_value = mock_graph
        mock_graph_impl.return_value = mock_graph

        # Call the method
        graph = GraphFactory.random_graph(n)

        # Assertions
        mock_barabasi_albert_graph.assert_called_once_with(n, int(n / 1.5))
        self.assertIsInstance(graph, Graph)

    @patch('api.services.graph_factory.nx.community.louvain_communities')
    @patch('api.services.graph_factory.nx.Graph')
    def test_topics_similarity_based_graph(self, mock_graph, mock_louvain_communities):
        # Setup mock for community detection
        name = 'test_graph'
        posts = {f"post_{i}": {"title": f"Post {i}", "url": f"https://example.com/{i}"} for i in range(5)}
        similarities = {
            "post_0": {"post_1": 0.9, "post_2": 0.8},
            "post_1": {"post_0": 0.9, "post_2": 0.7},
            "post_2": {"post_0": 0.8, "post_1": 0.7}
        }
        mock_graph_instance = nx.Graph()
        mock_louvain_communities.return_value = [[0, 1], [2]]
        mock_graph.return_value = mock_graph_instance

        # Call the method
        graph = GraphFactory.posts_similarity_based_graph(name, posts, similarities)

        # Assertions
        mock_louvain_communities.assert_called_once()
        self.assertIsInstance(graph, NetworkxGraphImpl)
        self.assertTrue(len(graph.graph.nodes) > 0)

    def test_create_comments_graph(self):
        # Setup sample input for create_comments_graph
        graph_name = 'test_comments_graph'
        post_text = "This is a post"
        comments = [
            {"_id": "comment_1", "text": "This is a positive comment", "sentiment": 2, "score": 10},
            {"_id": "comment_2", "text": "This is a neutral comment", "sentiment": 1, "score": 5},
            {"_id": "comment_3", "text": "This is a negative comment", "sentiment": 0, "score": 3},
        ]
        base_size = 15

        # Call the method
        graph = GraphFactory.create_comments_graph(graph_name, post_text, comments, base_size)

        # Assertions
        self.assertIsInstance(graph, NetworkxGraphImpl)
        self.assertEqual(len(graph.graph.nodes), 7)  # 4 nodes: post, 3 sentiment groups
        self.assertIn("group_positive", graph.graph.nodes)
        self.assertIn("group_negative", graph.graph.nodes)
        self.assertIn("group_neutral", graph.graph.nodes)

    def test_create_comments_graph_empty_comments(self):
        # Empty comments to test edge case
        graph_name = 'empty_comments_graph'
        post_text = "This is a post"
        comments = []
        base_size = 15

        # Call the method
        graph = GraphFactory.create_comments_graph(graph_name, post_text, comments, base_size)

        # Assertions
        self.assertIsInstance(graph, NetworkxGraphImpl)
        self.assertEqual(len(graph.graph.nodes), 4)  # Only post and sentiment groups
        self.assertIn("group_positive", graph.graph.nodes)
        self.assertIn("group_negative", graph.graph.nodes)
        self.assertIn("group_neutral", graph.graph.nodes)


if __name__ == '__main__':
    unittest.main()
