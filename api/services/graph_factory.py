import os

import networkx as nx
from pyvis.network import Network

from api.models.domain.graph_drawing import GraphDrawing
from api.models.domain.networkx_graph_impl import NetworkxDiGraphImpl


class GraphFactory:

    @staticmethod
    def random_graph(n):
        graph = NetworkxDiGraphImpl(f"random{n}barabasi", nx.barabasi_albert_graph(n, int(n/1.5)))
        return graph
#
# g = NetworkxDiGraphImpl('random100barabasi')
# pos = nx.spring_layout(g.graph)
#
# for i, node in enumerate(g.graph.nodes(data=True)):
#     node[1]["x"] = pos[str(i)][0]*1000
#     node[1]["y"] = pos[str(i)][1]*1000
#
# nt = Network('800', '800px')
# nt.from_nx(g.graph)
# nt.toggle_physics(False)
# nt.write_html(GraphDrawing.resolve_path('forceatlas_barabasi'))
