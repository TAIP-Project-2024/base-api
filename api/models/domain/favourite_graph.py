class FavouriteGraph:
    def __init__(self, graph_id, user_id,):
        self.graph_id = graph_id
        self.user_id = user_id

    def to_dict(self):
        return {
            "graph_id": self.graph_id,
            "user_id": self.user_id,
        }