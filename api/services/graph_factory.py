import networkx as nx


from api.models.domain.networkx_graph_impl import NetworkxGraphImpl
from api.services.layouts.design_config import COMMUNITY_COLORS


class GraphFactory:

    @staticmethod
    def assign_communities(graph, colors, strategy):
        if (strategy == 'louvain'):
            partitions = nx.community.louvain_communities(graph)
        else:
            raise Exception("unknown community detection strategy")

        print(f'detected {len(partitions)} partitions')
        if len(partitions) > len(colors):
            raise Exception("provide more colors :)")

        for i, partition in enumerate(partitions):
            for node in partition:
                graph.nodes[node]['color'] = colors[i]
                graph.nodes[node]['community'] = i

    @staticmethod
    def posts_similarity_based_graph(name, posts, similarities, t = 0, community_colors = COMMUNITY_COLORS, strategy = 'louvain'):
        """
        Args:
            name: name for the graph
            similarities: a similarity matrix
            t: similarity threshold
            community_colors: community colors
            returns a graph.
        """
        hairball = nx.Graph()

        edges_tuples = []
        for line in similarities.items():
            for value in line[1]:
                try:
                    if similarities[line[0]][value] > t and value != line[0]:
                            edges_tuples.append((line[0], value, similarities[line[0]][value]))
                except KeyError as ke:
                    print(1)
                    print(ke)
                    continue

        hairball.add_weighted_edges_from(edges_tuples)
        nx.set_node_attributes(hairball, posts)
        GraphFactory.assign_communities(hairball, community_colors, strategy)
        graph = NetworkxGraphImpl(name, hairball)

        return graph
    @staticmethod
    def create_comments_graph(graph_name, post_text, comments, colors, base_size = 15, post_node_size = 25, post_node_color = "yellow", group_size_factor = 30):
        """
        Args
        : post {text, url}
        : comments an array of objects that have an id,
        : colors - an array of colors negative, neutral and positive for comments
        a body and a sentiment rank
        {id, title, sentiment, group(0,1,2)}
        """
        groups = ["group_negative", "group_neutral", "group_positive"]
        graph = nx.Graph()
        graph.add_node("post", title=post_text, url="url", size = post_node_size, color = post_node_color)
        graph.add_node("group_neutral", label="Neutral", color=colors[1], size = base_size)
        graph.add_node("group_negative", label="Negative", color=colors[0], size = base_size)
        graph.add_node("group_positive", label="Positive", color=colors[2], size = base_size)
        graph.add_edges_from([("post", "group_neutral"), ("post", "group_positive"), ("post", "group_negative")])
        n = {}

        for group in groups:
            n[group] = 0

        for entry in comments:
            print(entry)
            sentiment = round(entry["sentiment"])
            group = groups[sentiment]
            label = "score " + str(entry["score"])
            graph.add_node(entry["_id"],
                           title = entry["text"],
                           label = label,
                           color = colors[sentiment],
                           group = group,
                           size = base_size,
                           hidden = True)

            graph.add_edge(group, entry["_id"])
            n[group] += 1

        for group in groups:
            try:
                graph.nodes[group]['size']=n[group]+group_size_factor
            except:
                pass # means no such members
        return NetworkxGraphImpl(graph_name, graph)

