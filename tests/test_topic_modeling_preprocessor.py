import unittest

from api.ml_core.data_preprocess.topic_modeling_preprocessor import TopicModelingPreprocessor
from api.ml_core.data_preprocess.corpus_processor import CorpusProcessor


class TopicModelingPreprocessorTest(unittest.TestCase):
    def setUp(self):
        self.preprocessor = TopicModelingPreprocessor()

    def test_emoji_elimination_equal(self):
        input_text = "This is an emoji 👍"
        output_text = "This is an emoji "
        self.assertEqual(self.preprocessor.emoji_elimination(input_text), output_text)

    def test_emoji_elimination_not_equal(self):
        input_text = "This is an emoji 👍"
        output_text = "This is an emoji"
        self.assertNotEqual(self.preprocessor.emoji_elimination(input_text), output_text)

    def test_remove_punctuation_equal(self):
        input_text = "Hello, world!"
        output_text = "Hello world"
        self.assertEqual(self.preprocessor.remove_punctuation(input_text), output_text)

    def test_remove_punctuation_not_equal(self):
        input_text = "Hello, world!"
        output_text = "Hello world!!!"
        self.assertNotEqual(self.preprocessor.remove_punctuation(input_text), output_text)

    def test_tokenize_equal(self):
        input_text = "This is a test"
        output_text = ["this", "is", "test"]
        self.assertEqual(self.preprocessor.tokenize(input_text), output_text)

    def test_tokenize_not_equal(self):
        input_text = "This is a test"
        output_text = ["This", "is", "test"]
        self.assertNotEqual(self.preprocessor.tokenize(input_text), output_text)

    def test_preprocessing_pipeline(self):
        input_text = "Here's an example text 😍! Visit https://example.com for more info. #exampleforhashtags"
        tokens = self.preprocessor.preprocess(input_text)
        output_tokens = ['here', 'example', 'text', 'visit', 'more', 'info', 'example', 'hash', 'tag']
        self.assertIsInstance(tokens, list)
        self.assertEqual(tokens, output_tokens)
