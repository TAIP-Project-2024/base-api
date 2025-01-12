from api.services.layouts.comments_drawing import CommentsDrawing

COMMUNITY_COLORS = [
    "#3C3ABF",
    "#86159A",
    "#004F8E",
    "#8F2C2E",
    "#980000",
    "#364A80",
    "#185B1B",
    "#3A5718",
    "#9C1341",
    "#065A4F"
]

#==========================
# Drawing design parameters
#==========================

ForceDirectedLouvain_kwargs = {
    "threshold": 3,
    "node_size": 15,
    "height": "100vh",
    "width": "100vw",
    "edge_weight_in_drawing": 1,
    "hover_size": 5,
    "n": 800,
    "bgcolor": "#ECEFF1"
}

CommunityStars_kwargs = {
    "physics": False,
    "height": "100vh",
    "width": "100vw",
    "community_weight": 1,
    "node_size": 10,
    "hub_node_size": 10,
    "topic_node_size": 30,
    "topic_hub_weight": 3,
    "n": 800,
    "bgcolor": "#ECEFF1"
}

CommentsDrawing_kwargs = {
    "node_size": 15,
    "height": "100vw",
    "width": "100vh",
    "edge_weight_in_drawing": 1,
    "hover_size": 5,
    "n": 800,
    "bgcolor": "white"
}

#==========================
# Graph parameters
#==========================

post_similarity_graph_kwargs = {
    "t" : 0,
    "community_colors" : COMMUNITY_COLORS,
    "strategy" : 'louvain'
}

comments_graph_kwargs = {
    "colors" : ["red", "gray", "green"],
    "base_size" : 15,
    "post_node_size" : 25,
    "post_node_color" : "yellow",
    "group_size_factor" : 30
}

#=============================
# File naming formats for files
#=============================

def comments_graph_name_format(post_id, topic):
    return f"post#{post_id}CommentsGraph{[topic]}"

def comments_graph_drawing_name_format(post_id, topic):
    return f"post#{post_id}CommentsGraphDrawing{[topic]}"

def posts_sim_graph_name_format(topic, timestamp):
    return f'{topic}_posts_sim_graph_{timestamp}'

def hairball_drawing_name_format(topic, timestamp):
    return f'{topic}_hairball_drawing_{timestamp}'

def community_drawing_name_format(topic, timestamp):
    return f'{topic}_community_drawing_{timestamp}'