from api.models.domain.graph_drawing import GraphDrawing


class GraphDrawingService:
    def __init__(self):
        pass

    def generate_drawing(self, layout, graph):
        """
        Will try to apply the layout algorithm for the graph
        Will return None if it fails.
        """
        # graph_drawing = GraphDrawing(graph).draw(layout)
        # return graph_drawing
        graph_drawing = GraphDrawing(graph)
        return graph_drawing.draw_as(layout)
