"""
    An object representing a layout (nodes, edges, and a unique
    displacement).
"""


class GraphDrawing:
    def __init__(self, graph):
        """
        @param graph: graph of models.Graph type
        """
        self.graph = graph
        self.graph_drawing = None

    def draw_as(self, layout):
        """
        A method implementing visitor design pattern for
        graph drawing using various layouts.
        @param layout: layout of the graph
        @return: the respective graph drawing
        """
        self.graph_drawing = layout.apply(self.graph)
        return self.graph_drawing
