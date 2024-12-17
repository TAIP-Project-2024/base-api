import os

import networkx as nx

from pyvis.network import Network

from api.models.domain.graph_drawing import GraphDrawing
from api.models.domain.networkx_graph_impl import NetworkxGraphImpl, NetworkxDiGraphImpl
from api.services.layouts.Layout import Layout


class CommunityStars(Layout):
    def __init__(self, topic, physics = False, height = 1000, width = 1000, community_weight = 1,
                 node_size = 10, hub_node_size = 10, topic_node_size = 30, topic_hub_weight = 3, n = 1000,
                 bgcolor = 'white'):
        """
        community_summaries: a list of titles indexed by the community index
        topic_hub_weight: weight of the edge connecting them
        community_weight: weight of the edge between a hub and a community node
        ...

        This layout needs a graph that already has the communities and colors
        as annotations
        """
        self.topic = topic
        self.physics = physics
        self.height = height
        self.width = width
        self.community_weight = community_weight
        self.node_size = node_size
        self.hub_node_size = hub_node_size
        self.topic_node_size = topic_node_size
        self.topic_hub_weight = topic_hub_weight
        self.n = n
        self.bgcolor = bgcolor

    def describe_communities(self, graph):
        graph = graph.graph
        communities = {}

        for node in graph.nodes(data = True):
            node = node[1]
            com = node['community']
            if com in communities:
                communities[com].append(node['title'])
            else:
                communities[com] = []
        # todo apply ML methods to describe many posts in a phrase
        # todo use an external api and store it in summaries
        # dummy:
        return {i : f'description of the community {i}' for i in communities.keys()}

    def apply(self, graph, html_file):
        community_summaries = self.describe_communities(graph)

        #disconnect all graphs
        graph = graph.graph
        nt = Network(self.height, self.width, bgcolor=self.bgcolor)
        graph.remove_edges_from(list(graph.edges))
        hub_nodes = {}
        hub_index = -1
        node_list = list(graph.nodes)
        for node in node_list:
            comm = graph.nodes[node]['community']
            if comm in hub_nodes:
                hub = hub_nodes[comm]
            else:
                hub = hub_index
                hub_index -= 1
                hub_nodes[comm] = hub
                graph.add_node(hub, community = comm, hub_node = True, label = community_summaries[comm],
                               font = {'color': '#FF10F0'})
            graph.add_edge(hub, node, weight = self.community_weight)
        nx.set_node_attributes(graph, self.node_size, 'size')

        graph.add_node(hub_index, size = self.topic_node_size, color = 'green', label = self.topic,
                       font = {'color':  '#ff4d4d'})

        graph.add_weighted_edges_from([(hub_index, i, self.topic_hub_weight) for i in hub_nodes.values()])

        pos = nx.kamada_kawai_layout(graph)


        for node in graph.nodes(data=True):
            node[1]["x"] = pos[node[0]][0]*self.n
            node[1]["y"] = pos[node[0]][1]*self.n
        nx.set_edge_attributes(graph, 0, "weight")
        try:
            nt.from_nx(graph)
            if not self.physics:
                nt.toggle_physics(False)
            self.load_interactions(nt)
            # process hover feature
            with open(html_file, "w+") as out:
                out.write(nt.html)
        except Exception as e:
            print(e)


cs = CommunityStars(
    topic = "TOPIC PLACEHOLDER",
    width = '100vw',
    height = '100vh',
    bgcolor = 'black',
    n = 800
)
gd = GraphDrawing(NetworkxGraphImpl('cool_graph'), 'communities_stars')
gd.draw_as(cs)