import networkx as nx

from api.services.general.graph_drawing_service import GraphDrawingService
from api.services.layouts.Layout import Layout

from django.test import TestCase

from api.services.layouts.simple_circular_drawing import SimpleCircularDrawing
import os
class GraphDrawingServiceTests(TestCase):
    def setUp(self):
        self.graph_drawing_service = GraphDrawingService()
        self.graph = nx.read_graphml("./resources/graphs/example.graphml")

    def  test_graph_drawing_service(self):
        layout = SimpleCircularDrawing()
        graph_drawing = self.graph_drawing_service.generate_drawing(layout, self.graph)
        self.assertNotEqual(graph_drawing, False)
