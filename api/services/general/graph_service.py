import networkx as nx
class GraphService:

    def __init__(self):
        pass

    def generate_nxgraph_from_metadata(self, metadata):
        """
        Will generate a graph connecting all reactions
        to the original post.
        Will have n+1 nodes, n - #reactions.
        """
        nodes = metadata['reactions']
        G = nx.DiGraph()
        G.add_node(0,
                                label = metadata['post'],
                                color = "blue",
                                title = metadata['author'])
        for i, node in enumerate(nodes):
            i = i + 1
            G.add_node(i, label = node["user"],
                       title = node["comment"],
                       color = self.compute_color(node["sentiment"]))
            G.add_edge(i, 0)
        nx.write_graphml(G, "resources/graphs/example.graphml")
        return G

    def save_graph(self, graph):
        pass

    def delete_graph(self, graph):
        pass

    def find_graph(self, id):
        None

    def compute_color(self, x):
        x = max(0, min(1, x))
        red = int(255 * (1 - x))
        green = int(255 * x)
        blue = 0
        hex_color = f'#{red:02x}{green:02x}{blue:02x}'
        return hex_color