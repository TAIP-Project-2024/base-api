import os

import networkx as nx

from api.models.domain.graph import Graph
from api.repositories.general.graph_repository import GraphRepository


class GraphService:

    def save_graph(self, graph, delete_local):
        if not graph.saved_locally:
            graph.save()

        with open(graph.graphml_file, 'rb') as file_buffer:
            with GraphRepository() as graph_repo:
                id = graph_repo.add(graph.name, file_buffer)

        graph.id = id
        try:
            if delete_local:
                os.remove(graph.graphml_file)
        except Exception as e:
            print(e)
        return id

    def check_exists(self, name):
        with GraphRepository() as gr:
            return gr.check_exists(name)

    def delete_graph(self, graph):
        with GraphRepository() as graph_repo:
            return graph_repo.delete(graph.name)

    def find_graph_buffer_by_name(self, name):
        with GraphRepository() as graph_repo:
            return graph_repo.get(name)

    def clear_comments_graphs_for_topic(self, topic):
        regex_pattern = '^post#[a-z0-9]{7}CommentsGraph'+f'\\[{topic}\\]'+'$'

        with GraphRepository() as gr:
            comments_graphs = gr.find_by_regex(regex_pattern)
            ids = [g._id for g in comments_graphs]
            if (len(ids) > 0):
                gr.delete_from_list(ids)

    def delete_all_except(self, keep):
        """
        deletes all graphs except those in the keep list
        """
        keep_set = set(keep)
        with GraphRepository() as gr:
            all_graphs = gr.get_all_names()
            for name in all_graphs:
                if name not in keep_set:
                    gr.delete(name)

    def fetch_graph_locally(self, name):
        with GraphRepository() as graph_repo:
            file_buffer = graph_repo.get(name)
            path = Graph.resolve_path(name)
            with open(path, 'wb') as file:
                # file.write(file_buffer.read())
                while True:
                    chunk = file_buffer.read(2048)
                    if not chunk:
                        break
                    file.write(chunk)


    def compute_color(self, x):
        """
        This computes a color based on x
        x = 1 => green
        x = 0 => red
        0 < x < 1 => intermediary
        """
        x = max(0, min(1, x))
        red = int(255 * (1 - x))
        green = int(255 * x)
        blue = 0
        hex_color = f'#{red:02x}{green:02x}{blue:02x}'
        return hex_color

#
# marvel_graph = NetworkxDiGraphImpl('marvel')
# GraphService().save_graph(marvel_graph, False)
# GraphService().clear_comments_graphs()
