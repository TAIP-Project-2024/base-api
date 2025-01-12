import unittest

from api.ml_core.sentiment_analysis.lexicon_sentiment_model import LexiconSentimentModel


class TestLexiconSentimentModel(unittest.TestCase):
    def setUp(self):
        self.model = LexiconSentimentModel()

    def test_init(self):
        self.assertIsNotNone(self.model)

    def test_analyze(self):
        # Given
        text = "I am happy"
        lexicon_sentiment_model = LexiconSentimentModel()

        # When
        result = lexicon_sentiment_model.analyze(text)

        # Then
        self.assertEqual(result['compound'], 0.5719)
        self.assertEqual(result['neg'], 0.0)
        self.assertEqual(result['neu'], 0.213)
        self.assertEqual(result['pos'], 0.787)