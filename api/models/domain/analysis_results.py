from datetime import datetime

class AnalysisResults:
    def __init__(self, sentiment_result, community_result, graph_result):
        self.sentiment_result = sentiment_result
        self.community_result = community_result
        self.graph_result = graph_result
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            "sentiment_result": self.sentiment_result,
            "community_result": self.community_result,
            "graph_result": self.graph_result,
            "created_at": self.created_at
        }
