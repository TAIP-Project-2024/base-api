import os
import unittest
import networkx as nx
from tempfile import NamedTemporaryFile
from api.services.layouts.force_directed_louvain import ForceDirectedLouvain


class TestForceDirectedLouvain(unittest.TestCase):
    def setUp(self):
        # Create a mock graph
        self.graph = nx.Graph()
        self.graph.add_nodes_from([1, 2, 3])
        self.graph.add_edge(1, 2, weight=0.5)
        self.graph.add_edge(2, 3, weight=0.8)
        self.graph.add_edge(3, 1, weight=0.2)

        # Create an instance of ForceDirectedLouvain
        self.layout = ForceDirectedLouvain(
            threshold=0.6,
            node_size=10,
            height=800,
            width=800,
            edge_weight_in_drawing=2,
            hover_size=7,
            n=1000,
            bgcolor="white"
        )

    def test_initialization(self):
        # Test the initialization of the layout object
        self.assertEqual(self.layout.threshold, 0.6)
        self.assertEqual(self.layout.node_size, 10)
        self.assertEqual(self.layout.height, 800)
        self.assertEqual(self.layout.width, 800)
        self.assertEqual(self.layout.edge_weight_in_drawing, 2)
        self.assertEqual(self.layout.hover_size, 7)
        self.assertEqual(self.layout.n, 1000)
        self.assertEqual(self.layout.bgcolor, "white")

    def test_apply(self):
        with NamedTemporaryFile(suffix=".html", delete=False) as temp_file:
            html_file = temp_file.name

        try:
            # Apply the layout to the graph
            class MockGraph:
                def __init__(self, graph):
                    self.graph = graph

            mock_graph = MockGraph(self.graph)
            self.layout.apply(mock_graph, html_file)

            # Verify that edges below the threshold are removed
            remaining_edges = list(mock_graph.graph.edges(data=True))
            self.assertEqual(len(remaining_edges), 1)
            self.assertIn((2, 3, {"width": 2, "hoverWidth": 7, "title": "Similarity between node 2 and node 3 - 0.8"}), remaining_edges)

            # Verify that node positions are updated
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
        # Test applying layout with an invalid graph (missing attributes)
        invalid_graph = nx.Graph()
        invalid_graph.add_nodes_from([1, 2, 3])
        invalid_graph.add_edges_from([(1, 2), (2, 3)])

        class MockGraph:
            def __init__(self, graph):
                self.graph = graph

        mock_graph = MockGraph(invalid_graph)

        with self.assertRaises(KeyError):
            self.layout.apply(mock_graph, "dummy_file.html")

    def test_apply_with_invalid_file_path(self):
        # Test applying layout with an invalid file path
        class MockGraph:
            def __init__(self, graph):
                self.graph = graph

        mock_graph = MockGraph(self.graph)

        invalid_path = "/invalid_path/dummy.html"
        with self.assertRaises(Exception):
            self.layout.apply(mock_graph, invalid_path)


if __name__ == "__main__":
    unittest.main()
