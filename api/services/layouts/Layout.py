from abc import abstractmethod


class Layout:
    @abstractmethod
    def apply(self, graph):
        """
        A layout algorithm that returns a graph
        drawing for the graph g
        @param graph: graph of type models.Graph to be drawn
        @return: a drawing of type models.GraphDrawing

        Note: we will create local html files, which can
        be deleted after being saved in the cloud.

        This is because we have to save them somewhere,
        most frameworks can't write to a buffer directly.
        """
        return None