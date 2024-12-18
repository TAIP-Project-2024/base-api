import unittest

from api.ml_core.sentiment_analysis.lstm_sentiment_model import LSTMSentimentModel


class LSTMSentimentModelTest(unittest.TestCase):
    def setUp(self):
        self.model = LSTMSentimentModel()

    def test_init(self):
        self.assertIsNotNone(self.model)

    def test_analyze(self):
        texts = ["This is a test", "This is another test"]
        sentiment_scores = self.model.analyze(texts)
        self.assertEqual(len(sentiment_scores), 2)
        self.assertTrue(all(isinstance(score, float) for score in sentiment_scores))
        self.assertTrue(all(0 <= score <= 1 for score in sentiment_scores))