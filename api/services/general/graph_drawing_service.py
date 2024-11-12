import os

from api.models.domain.graph_drawing import GraphDrawing
from api.repositories.general.graph_drawing_repository import DrawingRepository


class GraphDrawingService:
    def __init__(self):
        pass

    def generate_drawing(self, layout, graph):
        """
        Will try to apply the layout algorithm for the graph
        Will return false if it fails.
        """
        graph_drawing = GraphDrawing(graph)
        return graph_drawing.draw_as(layout)

    def save_graph_drawing(self, graph_drawing, delete_local=False):
        #retrieve the local file
        with open(graph_drawing.html_file, "rb") as f:
            #save to cloud
            DrawingRepository().add(graph_drawing.name, f)
        if delete_local:
            os.remove(graph_drawing.html_file)

    # todo delete drawing, etc.




