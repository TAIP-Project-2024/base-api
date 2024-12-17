import networkx as nx
from pyvis.network import Network

from api.services.layouts.Layout import Layout


class CommentsDrawing(Layout):
    def __init__(self, node_size = 15, height = 1000, width = 1000,
                 edge_weight_in_drawing = 1, hover_size = 5, n = 1000,
                 bgcolor = 'white'):
        """
        threshold: similarity threshold for edge pruning

        """
        self.node_size = node_size
        self.height = height
        self.width = width
        self.hover_size = hover_size
        self.n = n
        self.bgcolor = bgcolor

    def apply(self, graph, html_file):
        graph = graph.graph
        nt = Network(self.height, self.width)
        pos = nx.kamada_kawai_layout(graph)
        for node in graph.nodes(data=True):
            node[1]["x"] = pos[str(node[0])][0] * self.n
            node[1]["y"] = pos[str(node[0])][1] * self.n
        try:
            nt.from_nx(graph)
            nt.toggle_physics(False)

            show_comments_script = \
           """
        <script type="text/javascript">
        var groupVisibility = {};
        network.on('click', function (event) {
          if (event.nodes.length > 0) {
            var clickedNodeGroup = event.nodes[0];

            var isVisible = groupVisibility[clickedNodeGroup] !== false;

            nodes.forEach(function (node) {
              if (node.group === clickedNodeGroup) {
                var newVisibility = isVisible ? false : true;
                nodes.update({ id: node.id, hidden: newVisibility });
              }
            });

            // Update the visibility state for the group
            groupVisibility[clickedNodeGroup] = !isVisible;
          }
        });
        </script>
            
            """
            nt.html = nt.generate_html()
            nt.html = nt.html.replace("</body>", show_comments_script + '\n' + "</body>")
            with open(html_file, "w+") as out:
                out.write(nt.html)
        except Exception as e:
            print(e)
