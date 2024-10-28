# sentiment_analysis_result.py

class SentimentAnalysisResult:
    """Stores the results of sentiment analysis. Implements the
    Data Transfer Object (DTO) pattern for encapsulating data."""

    def __init__(self, text: str, sentiment: str, score: float):
        """
        Initializes a new instance of SentimentAnalysisResult.

        Args:
            text (str): The original text for which sentiment was analyzed.
            sentiment (str): The detected sentiment (e.g., 'positive', 'negative', 'neutral').
            score (float): The confidence score of the detected sentiment.
        """
        self.text = text  # The original text
        self.sentiment = sentiment  # Detected sentiment
        self.score = score  # Confidence score

    def to_dict(self):
        """Converts the result to a dictionary for easy serialization."""
        return {
            'text': self.text,
            'sentiment': self.sentiment,
            'score': self.score,
        }
