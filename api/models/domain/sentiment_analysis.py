import random
from datetime import datetime


class SentimentAnalysis:
    def __init__(self):
        self.sentiment_score = None
        self.timestamp = None

    def analyze(self, data):
        """Simulate sentiment sentiment_analysis and set the result."""
        self.sentiment_score = random.uniform(-1, 1)
        self.timestamp = datetime.now()
        return self.to_dict()

    def get_sentiment_score(self):
        return self.sentiment_score

    def get_timestamp(self):
        return self.timestamp

    def set_sentiment_score(self, score):
        self.sentiment_score = score

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def to_dict(self):
        """Return the object's attributes as a dictionary."""
        return {
            "sentiment_score": self.sentiment_score,
            "timestamp": self.timestamp
        }
