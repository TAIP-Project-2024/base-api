import networkx as nx

from pyvis.network import Network

from api.services.layouts.Layout import Layout


class SimpleCircularDrawing(Layout):

    def apply(self, graph):
        nt = Network('500px', '500px')
        pos = nx.circular_layout(graph)
        for i, node in enumerate(graph.nodes(data=True)):
            node[1]["x"] = pos[str(i)][0]
            node[1]["y"] = pos[str(i)][1]

        nt.from_nx(graph)
        nt.write_html("resources/drawings/circular.html")
        return True