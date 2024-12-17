import networkx as nx

from api.services.general.graph_drawing_service import GraphDrawingService
from api.services.layouts.Layout import Layout

from django.test import TestCase
import os


class GraphDrawingServiceTests(TestCase):
    def setUp(self):
        self.graph_drawing_service = GraphDrawingService()
        self.graph = nx.read_graphml("./resources/graphs/example.graphml")
