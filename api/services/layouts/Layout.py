from abc import abstractmethod


class Layout:
    @abstractmethod
    def apply(self, graph, html_file):
        """
        A layout algorithm that returns a graph
        drawing for the graph g
        @param graph: graph of type models.Graph to be drawn
        @param html_file: html file
        @return: a drawing of type models.GraphDrawing

        Note: we will create local html files, which can
        be deleted after being saved in the cloud.

        This is because we have to save them somewhere,
        most frameworks can't write to a buffer directly.
        """
        return None

    def load_interactions(self, nt, topic):
        """
        This event listener sends the information about a node
        being pressed to the parent window, to propagate information
        """
        ops = """        "hover": true,"""
        anchor = """ "dragNodes": true,"""
        script = \
            f"""
        <script type="text/javascript">

        network.on("hoverNode", function (params) {{
            const nodeId = params.node;
            defaultSize = data.nodes.get(nodeId)['size'];
            data.nodes.update({{ id: nodeId, defaultSize: defaultSize, size: defaultSize * 3 }});
        }});
        network.on("blurNode", function (params) {{
            const nodeId = params.node;
            size = data.nodes.get(nodeId)['size'];
            data.nodes.update({{ id: nodeId, size: size / 3 }});
        }});
        network.on("selectNode", function (params) {{
            if (params.nodes.length > 0) {{
                const nodeId = params.nodes[0]; // Get the clicked node's ID
                const node = data.nodes.get(nodeId); 
                const message = {{
                    type: "nodeClick",  
                    nodeId: nodeId,      
                    url: node.url || "",  
                    title: node.title,
                    topic: "{topic}"
                }};
                window.parent.postMessage(message, "*");
            }}
        }});
        </script>
        """

        nt.html = nt.generate_html()
        nt.html = nt.html.replace(anchor, anchor + '\n' + ops + '\n')
        nt.html = nt.html.replace("</body>", script + '\n' + "</body>")

