import unittest

from api.ml_core.sentiment_analysis.bert_sentiment_model import BertSentimentModel


class BertSentimentModelTest(unittest.TestCase):
    def setUp(self):
        self.model = BertSentimentModel()

    def test_init(self):
        self.assertIsNotNone(self.model)

    def test_analyze(self):
        text = "This is a test"
        sentiment_score, sentiment_label = self.model.analyze(text)
        self.assertIsNotNone(sentiment_score)
        self.assertIsNotNone(sentiment_label)
        self.assertTrue(isinstance(sentiment_score, float))
        self.assertTrue(isinstance(sentiment_label, str))
        self.assertGreaterEqual(sentiment_score, 0)
        self.assertLessEqual(sentiment_score, 2)
        self.assertIn(sentiment_label, ['negative', 'neutral', 'positive'])
