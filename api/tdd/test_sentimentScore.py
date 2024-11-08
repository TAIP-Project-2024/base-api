import unittest
from api.mdd.mdd2.SentimentScore import SentimentScore

class TestSentimentScore(unittest.TestCase):
    def test_initialization_default(self):
        score = SentimentScore()
        self.assertEqual(score.score, 0.0)
        self.assertEqual(score.polarity,0.0)

    def test_initialization(self):
        score = SentimentScore(polarity=0.7,score=0.8)
        self.assertEqual(score.score,0.8)
        self.assertEqual(score.polarity,0.7)

    def test_get_sentiment_positive(self):
        score = SentimentScore(polarity=0.8)
        self.assertEqual(score.get_sentiment(),"Positive")

    def test_get_sentiment_negative(self):
        score = SentimentScore(polarity=-0.5)
        self.assertEqual(score.get_sentiment(),"Negative")

    def test_get_sentiment_neutral(self):
        score = SentimentScore(polarity=0.0)
        self.assertEqual(score.get_sentiment(),"Neutral")

    def test_very_positive(self):
        sentiment = SentimentScore(polarity=0.8, score=0.7)
        self.assertEqual(sentiment.get_detailed_sentiment(), "Very Positive")

    def test_slightly_positive(self):
        sentiment = SentimentScore(polarity=0.4, score=0.4)
        self.assertEqual(sentiment.get_detailed_sentiment(), "Slightly Positive")

    def test_very_negative(self):
        sentiment = SentimentScore(polarity=-0.7, score=-0.6)
        self.assertEqual(sentiment.get_detailed_sentiment(), "Very Negative")

    def test_slightly_negative(self):
        sentiment = SentimentScore(polarity=-0.3, score=-0.4)
        self.assertEqual(sentiment.get_detailed_sentiment(), "Slightly Negative")

    def test_neutral_detailed(self):
        # Neutral polarity and score
        sentiment = SentimentScore(polarity=0.0, score=0.0)
        self.assertEqual(sentiment.get_detailed_sentiment(), "Neutral")