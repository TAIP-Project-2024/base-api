from abc import abstractmethod


class GraphLayout:
    @abstractmethod
    def apply(self, graph):
        """
        A layout algorithm that returns a graph
        drawing for the graph g
        @param graph: graph of type models.Graph to be drawn
        @return: a drawing of type models.GraphDrawing
        """
        pass