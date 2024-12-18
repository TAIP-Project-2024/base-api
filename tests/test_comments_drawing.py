import os
import unittest
import networkx as nx
from tempfile import NamedTemporaryFile
from api.services.layouts.comments_drawing import CommentsDrawing


class TestCommentsDrawing(unittest.TestCase):
    def setUp(self):
        # Create a sample graph
        self.graph = nx.Graph()
        self.graph.add_nodes_from([
            (1, {"label": "Node 1"}),
            (2, {"label": "Node 2"}),
            (3, {"label": "Node 3"})
        ])
        self.graph.add_edges_from([
            (1, 2, {"weight": 0.5}),
            (2, 3, {"weight": 0.8}),
            (3, 1, {"weight": 0.2})
        ])

        # Create an instance of CommentsDrawing
        self.layout = CommentsDrawing(
            node_size=15,
            height=800,
            width=800,
            hover_size=5,
            n=1000,
            bgcolor="white"
        )

    def test_initialization(self):
        # Test if the layout is initialized with correct parameters
        self.assertEqual(self.layout.node_size, 15)
        self.assertEqual(self.layout.height, 800)
        self.assertEqual(self.layout.width, 800)
        self.assertEqual(self.layout.hover_size, 5)
        self.assertEqual(self.layout.n, 1000)
        self.assertEqual(self.layout.bgcolor, "white")

    def test_apply(self):
        # Test applying the layout and generating an HTML file
        with NamedTemporaryFile(suffix=".html", delete=False) as temp_file:
            html_file = temp_file.name

        try:
            class MockGraph:
                def __init__(self, graph):
                    self.graph = graph

            mock_graph = MockGraph(self.graph)

            # Apply the layout
            self.layout.apply(mock_graph, html_file)

            # Verify node positions
            for node, data in mock_graph.graph.nodes(data=True):
                self.assertIn("x", data)
                self.assertIn("y", data)

            # Verify that the HTML file is created
            self.assertTrue(os.path.exists(html_file))
            with open(html_file, "r") as f:
                html_content = f.read()
                self.assertIn("<html>", html_content)
                self.assertIn("</script>", html_content)  # Verify custom script addition

        finally:
            # Clean up the temporary file
            if os.path.exists(html_file):
                os.remove(html_file)

    def test_apply_with_invalid_file_path(self):
        # Test handling invalid file paths
        class MockGraph:
            def __init__(self, graph):
                self.graph = graph

        mock_graph = MockGraph(self.graph)

        with self.assertRaises(Exception):
            self.layout.apply(mock_graph, "/invalid_path/dummy.html")

    def test_apply_with_empty_graph(self):
        # Test applying the layout to an empty graph
        empty_graph = nx.Graph()
        class MockGraph:
            def __init__(self, graph):
                self.graph = graph

        mock_graph = MockGraph(empty_graph)

        with NamedTemporaryFile(suffix=".html", delete=False) as temp_file:
            html_file = temp_file.name

        try:
            self.layout.apply(mock_graph, html_file)

            # Verify no exceptions are raised and an HTML file is still created
            self.assertTrue(os.path.exists(html_file))
            with open(html_file, "r") as f:
                html_content = f.read()
                self.assertIn("<html>", html_content)
        finally:
            if os.path.exists(html_file):
                os.remove(html_file)


if __name__ == "__main__":
    unittest.main()
