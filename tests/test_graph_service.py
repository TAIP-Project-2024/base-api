import uuid

from django.test import TestCase

from api.models.domain.graph import Graph
from api.models.domain.networkx_graph_impl import NetworkxGraphImpl
from api.services.general.graph_drawing_service import GraphDrawingService
from api.services.general.graph_service import GraphService


class GraphServiceTests(TestCase):
    def setUp(self):
        self.graph_service = GraphService()
        self.graph = NetworkxGraphImpl("marvel2")
        self.graph_service.save_graph(self.graph, delete_local=False)
        self.reactions = [{"user": "user1", "comment": "I like it!", "sentiment": 0.7},
                     {"user": "user2", "comment": "I like it a bit!", "sentiment": 0.6},
                     {"user": "user3", "comment": "I used to like it", "sentiment": 0.5},
                     {"user": "user4", "comment": "I hardly like it!", "sentiment": 0.4},
                     {"user": "user5", "comment": "I like smth else!", "sentiment": 0.3},
                     {"user": "user6", "comment": "I don't like it!", "sentiment": 0.2},
                     {"user": "user7", "comment": "I'm against!", "sentiment": 0.1},
                     {"user": "user8", "comment": "I hate it!", "sentiment": 0.0}]


    def test_find_existing_graph(self):
        g = self.graph_service.check_exists("marvel2")
        self.assertEqual(g, True)

    def test_find_non_existing_graph(self):
        id = uuid.uuid4()
        g = self.graph_service.check_exists(id.__str__())
        self.assertEqual(g, False)

    def test_save_graph(self):
        g1 = NetworkxGraphImpl("marvel2")
        self.graph_service.save_graph(g1, delete_local=False)
        self.assertEqual(True, self.graph_service.check_exists("marvel2"))
