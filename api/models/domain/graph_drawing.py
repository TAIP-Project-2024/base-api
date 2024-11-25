"""
    An object representing a layout (nodes, edges, and a unique
    displacement).
"""
import os

from BaseAPI.settings import BASE_DIR


class GraphDrawing:
    def __init__(self, graph, name):
        """
        @param graph: graph of models.Graph type
        """
        self.graph = graph
        self.html_file = GraphDrawing.resolve_path(name)
        if not os.path.isfile(self.html_file):
            self.is_drawn = False
        else:
            self.is_drawn = True

        self.name = name



    def draw_as(self, layout):
        """
        A method implementing visitor design pattern for
        graph drawing using various layouts.
        @param layout: layout of the graph
        @return: the respective graph drawing
        """
        if self.graph is None:
            # todo exception
            return None
        layout.apply(self.graph, self.html_file)
        self.is_drawn = True
        return self.html_file

    @staticmethod
    def resolve_path(name):
        return str(BASE_DIR / (os.environ.get('LOCAL_DRAWINGS_DIR') + name + '.html'))
