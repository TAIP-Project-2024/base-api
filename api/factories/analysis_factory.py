from models.sentiment_analysis import SentimentAnalysis
from models.community_detection import CommunityDetection
from models.graph_representation import GraphRepresentation


class AnalysisFactory:
    @staticmethod
    def create_analysis_component(component_type):
        """Factory Method Pattern: Returns a specific sentiment_analysis component based on the requested type."""
        if component_type == "sentiment_analysis":
            return SentimentAnalysis()
        elif component_type == "community_detection":
            return CommunityDetection()
        elif component_type == "graph_representation":
            return GraphRepresentation()
        else:
            raise ValueError("Unknown sentiment_analysis component")
