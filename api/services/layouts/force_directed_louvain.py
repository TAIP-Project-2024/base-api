import os

import networkx as nx

from pyvis.network import Network

from api.services.layouts.Layout import Layout
from api.services.layouts.design_config import ForceDirectedLouvain_kwargs


class ForceDirectedLouvain(Layout):
    def __init__(self, topic, threshold, node_size = 15, height = '100vh', width = '100vw',
                 edge_weight_in_drawing = 1, hover_size = 5, n = 1000,
                 bgcolor = 'white'):
        """
        threshold: similarity threshold for edge pruning

        """
        self.threshold = threshold
        self.topic = topic
        self.node_size = node_size
        self.height = height
        self.width = width
        self.edge_weight_in_drawing = edge_weight_in_drawing
        self.hover_size = hover_size
        self.n = n
        self.bgcolor = bgcolor

    def apply(self, graph, html_file):
        graph = graph.graph
        nt = Network(self.height, self.width, bgcolor=self.bgcolor)
        nx.set_node_attributes(graph, self.node_size, 'size')
        edges_to_remove = []
        for edge in graph.edges(data=True):
            if edge[2]['weight'] >= self.threshold:
                edge[2]['hoverWidth'] = self.hover_size
                edge[2]['title'] = f'{edge[2]["weight"]}'
                continue
            edges_to_remove.append(edge)
        graph.remove_edges_from(edges_to_remove)
        pos = nx.kamada_kawai_layout(graph)
        nx.set_edge_attributes(graph, self.edge_weight_in_drawing, 'weight')

        for node in graph.nodes(data=True):
            node[1]["x"] = pos[node[0]][0] * self.n
            node[1]["y"] = pos[node[0]][1] * self.n
        try:
            nt.from_nx(graph)
            nt.toggle_physics(False)
            self.load_interactions(nt, self.topic)
            with open(html_file, "w+") as out:
                out.write(nt.html)

        except Exception as e:
            print(f"An error occurred: {e}")
            raise

#
# gd = GraphDrawing(NetworkxGraphImpl('40_random_posts'), '40_communities_hairball')
# gd.draw_as(ForceDirectedLouvain(0,
# #                                 bgcolor = '#ECEFF1',
#                                 n = 800))
