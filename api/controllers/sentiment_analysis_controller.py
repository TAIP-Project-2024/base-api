from factories.analysis_factory import AnalysisFactory
from models.analysis_results import AnalysisResults
from repositories.mongo_repository import MongoRepository
from datetime import datetime

class SentimentAnalysisController:
    def __init__(self):
        # Using the Repository Pattern to manage MongoDB operations
        self.repository = MongoRepository()

    def run_analysis(self):
        data = self.fetch_social_media_data()
        processed_data = self.preprocess_data(data)

        # Apply sentiment analysis using Factory Pattern
        sentiment_analyzer = AnalysisFactory.create_analysis_component("sentiment_analysis")
        sentiment_result = sentiment_analyzer.analyze(processed_data)

        # Apply community detection using Factory Pattern
        community_detector = AnalysisFactory.create_analysis_component("community_detection")
        community_result = community_detector.detect_communities(processed_data)

        # Generate graph representation using Factory Pattern
        graph_generator = AnalysisFactory.create_analysis_component("graph_representation")
        graph_result = graph_generator.generate_graph(processed_data)

        # Store results in MongoDB
        analysis_result = AnalysisResults(sentiment_result, community_result, graph_result)
        self.repository.create(analysis_result.to_dict())
        print("Data saved to MongoDB")

    def fetch_social_media_data(self):
        # Simulate fetching live social media data
        return {"data": "sample data"}

    def preprocess_data(self, data):
        # Simulate data preprocessing
        return {"preprocessed_data": data["data"] + " processed"}

    def view_results(self):
        # Read from MongoDB and display saved data
        query = {}  # Customize the query if needed
        results = self.repository.read(query)
        for result in results:
            print(result)

    def close(self):
        self.repository.close()
