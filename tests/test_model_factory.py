import unittest

from api.ml_core.models.model_factory import ModelFactory


class ModelFactoryTest(unittest.TestCase):
    def test_create_model_sentiment_lexicon(self):
        model = ModelFactory.create_model('sentiment', 'lexicon')
        self.assertIsNotNone(model)

    def test_create_model_sentiment_bert(self):
        model = ModelFactory.create_model('sentiment', 'bert')
        self.assertIsNotNone(model)

    def test_create_model_sentiment_lstm(self):
        model = ModelFactory.create_model('sentiment', 'lstm')
        self.assertIsNotNone(model)

    def test_create_model_topic_lda(self):
        model = ModelFactory.create_model('topic', 'lda')
        self.assertIsNotNone(model)

    def test_create_model_unknown_category(self):
        with self.assertRaises(ValueError):
            ModelFactory.create_model('unknown', 'lda')

    def test_create_model_unknown_type(self):
        with self.assertRaises(ValueError):
            ModelFactory.create_model('sentiment', 'unknown')
