import os
import unittest
from tempfile import NamedTemporaryFile

import networkx as nx

from api.services.layouts.community_stars import CommunityStars


class TestCommunityStars(unittest.TestCase):
    def setUp(self):
        # Create a mock graph with communities
        self.graph = nx.Graph()
        self.graph.add_nodes_from([
            (1, {"title": "Node 1", "community": 0}),
            (2, {"title": "Node 2", "community": 0}),
            (3, {"title": "Node 3", "community": 1}),
            (4, {"title": "Node 4", "community": 1}),
            (5, {"title": "Node 5", "community": 2}),
        ])
        self.graph.add_edges_from([(1, 2), (3, 4), (4, 5)])

        # Create an instance of CommunityStars
        self.layout = CommunityStars(
            topic="Test Topic",
            physics=False,
            height=800,
            width=800,
            community_weight=2,
            node_size=15,
            hub_node_size=20,
            topic_node_size=30,
            topic_hub_weight=3,
            n=1000,
            bgcolor="white",
        )

    def test_initialization(self):
        # Test the initialization of the layout object
        self.assertEqual(self.layout.topic, "Test Topic")
        self.assertFalse(self.layout.physics)
        self.assertEqual(self.layout.height, 800)
        self.assertEqual(self.layout.width, 800)
        self.assertEqual(self.layout.community_weight, 2)
        self.assertEqual(self.layout.node_size, 15)
        self.assertEqual(self.layout.hub_node_size, 20)
        self.assertEqual(self.layout.topic_node_size, 30)
        self.assertEqual(self.layout.topic_hub_weight, 3)
        self.assertEqual(self.layout.n, 1000)
        self.assertEqual(self.layout.bgcolor, "white")

    def test_describe_communities(self):
        # Test the describe_communities method
        class MockGraph:
            def __init__(self, graph):
                self.graph = graph

        mock_graph = MockGraph(self.graph)
        community_descriptions = CommunityStars.describe_communities(mock_graph)
        expected_descriptions = {
            0: "description of the community 0",
            1: "description of the community 1",
            2: "description of the community 2",
        }
        self.assertEqual(community_descriptions, expected_descriptions)

    def test_apply(self):
        # Test the apply method
        with NamedTemporaryFile(suffix=".html", delete=False) as temp_file:
            html_file = temp_file.name

        try:
            class MockGraph:
                def __init__(self, graph):
                    self.graph = graph

            mock_graph = MockGraph(self.graph)
            self.layout.apply(mock_graph, html_file)

            # Verify the graph is modified as expected
            # Check that hub nodes are added
            hub_nodes = [node for node, data in mock_graph.graph.nodes(data=True) if "hub_node" in data]
            self.assertEqual(len(hub_nodes), 3)  # One hub per community

            # Check that the topic node is added
            topic_nodes = [node for node, data in mock_graph.graph.nodes(data=True) if data.get("label") == "Test Topic"]
            self.assertEqual(len(topic_nodes), 1)

            # Check that the positions are updated
            for node, data in mock_graph.graph.nodes(data=True):
                self.assertIn("x", data)
                self.assertIn("y", data)

            # Check that the HTML file is generated
            self.assertTrue(os.path.exists(html_file))
            with open(html_file, "r") as f:
                html_content = f.read()
                self.assertIn("<html>", html_content)
                self.assertIn("<body>", html_content)
        finally:
            # Clean up the temporary file
            if os.path.exists(html_file):
                os.remove(html_file)

    def test_apply_with_invalid_graph(self):
        # Test the apply method with an invalid graph
        invalid_graph = nx.Graph()
        invalid_graph.add_node(1, title="Node 1")  # Missing 'community' attribute

        class MockGraph:
            def __init__(self, graph):
                self.graph = graph

        mock_graph = MockGraph(invalid_graph)

        with self.assertRaises(KeyError):
            self.layout.apply(mock_graph, "dummy_file.html")

    def test_apply_with_invalid_file_path(self):
        # Test the apply method with an invalid file path
        class MockGraph:
            def __init__(self, graph):
                self.graph = graph

        mock_graph = MockGraph(self.graph)

        invalid_path = "/invalid_path/dummy.html"
        with self.assertRaises(Exception):
            self.layout.apply(mock_graph, invalid_path)


if __name__ == "__main__":
    unittest.main()
