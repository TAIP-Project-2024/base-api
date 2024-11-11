"""
    An object representing a layout (nodes, edges, and a unique
    displacement).
"""


class GraphDrawing:
    def __init__(self, graph, name = None):
        """
        @param graph: graph of models.Graph type
        """
        self.graph = graph
        self.html_file = None
        self.name = name



    def draw_as(self, layout):
        """
        A method implementing visitor design pattern for
        graph drawing using various layouts.
        @param layout: layout of the graph
        @return: the respective graph drawing
        """
        self.html_file = layout.apply(self.graph)
        return self.html_file
