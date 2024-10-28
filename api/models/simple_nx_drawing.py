from api.models.Layout import GraphLayout
from api.models.graph import Graph
from api.models.graph_drawing import GraphDrawing
from pyvis.network import Network


class SimpleNxDrawing(GraphLayout):

    def apply(self, graph):
        nt = Network('500px', '500px')
        nt.from_nx(graph.graph)
        nt.write_html("../../resources/drawings/simple_drawing.html")