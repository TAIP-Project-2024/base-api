from api.models.domain.graph import Graph
from api.services.general.graph_drawing_service import GraphDrawingService
from api.services.layouts.Layout import Layout

from django.test import TestCase


class GraphDrawingServiceTests(TestCase):
    def setUp(self):
        self.graph_drawing_service = GraphDrawingService()
        self.graph = Graph("../resources/graphs/marvel.graphml")

    def test_graph_drawing_service(self):
        layout = Layout()
        graph_drawing = self.graph_drawing_service.generate_drawing(layout, self.graph)
        self.assertNotEqual(graph_drawing, None)
