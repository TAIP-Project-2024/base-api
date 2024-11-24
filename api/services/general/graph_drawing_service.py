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
        if not graph_drawing.is_drawn:
            # todo exception
            return

        with open(graph_drawing.html_file, "rb") as file_buffer:
            #save to cloud
            with DrawingRepository() as drawing_repository:
                drawing_repository.add(graph_drawing.name, file_buffer)
        if delete_local:
            os.remove(graph_drawing.html_file)

    def find_drawing_by_name(self, name):
        with DrawingRepository() as drawing_repository:
            file = drawing_repository.get(name)
        return file

    # todo delete drawing, etc.

