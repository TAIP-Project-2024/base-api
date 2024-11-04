import uuid

from django.test import TestCase

from api.models.domain.graph import Graph
from api.services.general.graph_drawing_service import GraphDrawingService
from api.services.general.graph_service import GraphService


class GraphServiceTests(TestCase):
    def setUp(self):
        self.graph_service = GraphService()
        self.graph = Graph("../resources/graphs/marvel.graphml")
        self.graph_service.save_graph(self.graph)

    def test_generate_graph(self):
        metadata = "resources/metadata/1"
        graph = self.graph_service.generate_graph_from_metadata(metadata)
        self.assertNotEqual(graph, None)

    def test_find_existing_graph(self):
        g = self.graph_service.find_graph(self.graph.id)
        self.assertNotEqual(g, None)

    def test_find_non_existing_graph(self):
        id = uuid.uuid4()
        g = self.graph_service.find_graph(id)
        self.assertEqual(g, None)

    def test_save_graph(self):
        g1 = Graph("../resources/graphs/marvel.graphml")
        self.graph_service.save_graph(g1)
        self.assertEqual(g1, self.graph_service.find_graph(g1.id))

    def test_delete_graph(self):
        self.graph_service.delete_graph(self.graph.id)
        self.assertEqual(None, self.graph_service.find_graph(self.graph.id))
