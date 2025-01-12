import unittest

from api.ml_core.sentiment_analysis.sentiment_model_interface import SentimentModelInterface


class SentimentModelInterfaceTest(unittest.TestCase):
    def test_analyze(self):
        sentiment_model_interface = SentimentModelInterface()
        with self.assertRaises(NotImplementedError):
            sentiment_model_interface.analyze("This is a test")