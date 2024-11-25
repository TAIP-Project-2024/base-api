import uuid

from django.test import TestCase

from api.models.domain.graph import Graph
from api.services.general.graph_drawing_service import GraphDrawingService
from api.services.general.graph_service import GraphService
from api.services.general.metadata_service import MetadataService


class GraphServiceTests(TestCase):
    def setUp(self):
        self.graph_service = GraphService()
        self.graph = Graph("../resources/graphs/marvel2.graphml")
        self.graph_service.save_graph(self.graph)
        self.reactions = [{"user": "user1", "comment": "I like it!", "sentiment": 0.7},
                     {"user": "user2", "comment": "I like it a bit!", "sentiment": 0.6},
                     {"user": "user3", "comment": "I used to like it", "sentiment": 0.5},
                     {"user": "user4", "comment": "I hardly like it!", "sentiment": 0.4},
                     {"user": "user5", "comment": "I like smth else!", "sentiment": 0.3},
                     {"user": "user6", "comment": "I don't like it!", "sentiment": 0.2},
                     {"user": "user7", "comment": "I'm against!", "sentiment": 0.1},
                     {"user": "user8", "comment": "I hate it!", "sentiment": 0.0}]
        self.metadata = MetadataService.generate_metadata_for_post(
            "mr author", "Bananas are tasty", self.reactions)

    def test_generate_graph(self):
        graph = self.graph_service.generate_nxgraph_from_metadata(self.metadata)
        self.assertNotEquals(graph, None)


    def test_number_of_nodes(self):
        graph = self.graph_service.generate_nxgraph_from_metadata(self.metadata)
        if graph is None:
            number_of_nodes = 0
        else:
            number_of_nodes = len(graph.nodes)
        self.assertEquals(number_of_nodes, self.reactions.__len__() + 1)

    def test_find_existing_graph(self):
        g = self.graph_service.find_graph(self.graph.id)
        self.assertNotEqual(g, None)

    def test_find_non_existing_graph(self):
        id = uuid.uuid4()
        g = self.graph_service.find_graph(id)
        self.assertEqual(g, None)

    def test_save_graph(self):
        g1 = Graph("../resources/graphs/marvel2.graphml")
        self.graph_service.save_graph(g1)
        self.assertEqual(g1, self.graph_service.find_graph(g1.id))

    def test_delete_graph(self):
        self.graph_service.delete_graph(self.graph.id)
        self.assertEqual(None, self.graph_service.find_graph(self.graph.id))
