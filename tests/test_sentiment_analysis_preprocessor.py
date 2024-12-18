import unittest

from api.ml_core.data_preprocess.topic_modeling_preprocessor import SentimentAnalysisPreprocessor


class SentimentAnalysisPreprocessorTest(unittest.TestCase):
    def setUp(self):
        self.preprocessor = SentimentAnalysisPreprocessor()

    def test_convert_abbreviations_equal(self):
        input_text = "brb"
        output_text = "be right back"
        self.assertEqual(self.preprocessor.convert_abbreviations(input_text), output_text)

    def test_convert_abbreviations_not_equal(self):
        input_text = "brb"
        output_text = "brb"
        self.assertNotEqual(self.preprocessor.convert_abbreviations(input_text), output_text)

    def test_convert_emojis_equal(self):
        input_text = "This is a 😀"
        output_text = "This is a :grinning_face:"
        self.assertEqual(self.preprocessor.convert_emojis(input_text), output_text)

    def test_convert_emojis_not_equal(self):
        input_text = "This is a 😍"
        output_text = "This is a :grinning_face:"
        self.assertNotEqual(self.preprocessor.convert_emojis(input_text), output_text)

    def test_remove_special_characters_equal(self):
        input_text = "This is a test!"
        output_text = "This is a test "
        self.assertEqual(self.preprocessor.remove_special_characters(input_text), output_text)

    def test_remove_special_characters_not_equal(self):
        input_text = "This is a test!"
        output_text = "This is a test!"
        self.assertNotEqual(self.preprocessor.remove_special_characters(input_text), output_text)

    def test_tokenize_equal(self):
        input_text = "This is a test"
        output_text = ["This", "is", "a", "test"]
        self.assertEqual(self.preprocessor.tokenize(input_text), output_text)

    def test_tokenize_not_equal(self):
        input_text = "This is a test"
        output_text = ["This", "is", "test"]
        self.assertNotEqual(self.preprocessor.tokenize(input_text), output_text)

    def test_preprocessing_pipeline(self):
        input_text = "Here's an example text 😍! Visit https://example.com for more info. #exampleforhashtags"
        tokens = self.preprocessor.preprocess(input_text)
        output_tokens = ['here', 'is', 'an', 'example', 'text', 'smiling', 'face', 'with', 'heart',
                         'eyes', 'visit', 'for', 'more', 'info', 'example', 'for', 'hash', 'tags']
        self.assertIsInstance(tokens, list)
        self.assertEqual(tokens, output_tokens)

    def test_preprocessing_pipeline_stopwords(self):
        input_text = "Here's an example text 😍! Visit https://example.com for more info. #exampleforhashtags"
        tokens = self.preprocessor.preprocess(input_text, remove_stopwords=True)
        output_tokens = ['example', 'text', 'smiling', 'face', 'heart', 'eyes', 'visit', 'info', 'example', 'hash', 'tags']
        self.assertIsInstance(tokens, list)
        self.assertEqual(tokens, output_tokens)

    def test_preprocessing_pipeline_lemmatize(self):
        input_text = "Here's an example text 😍! Visit https://example.com for more info. #exampleforhashtags"
        tokens = self.preprocessor.preprocess(input_text, lemmatize=True)
        output_tokens = ['here', 'be', 'an', 'example', 'text', 'smile', 'face', 'with', 'heart',
                         'eye', 'visit', 'for', 'more', 'info', 'example', 'for', 'hash', 'tag']
        self.assertIsInstance(tokens, list)
        self.assertEqual(tokens, output_tokens)

    def test_preprocessing_pipeline_stopwords_lemmatize(self):
        input_text = "Here's an example text 😍! Visit https://example.com for more info. #exampleforhashtags"
        tokens = self.preprocessor.preprocess(input_text, remove_stopwords=True, lemmatize=True)
        output_tokens = ['example', 'text', 'smile', 'face', 'heart', 'eye', 'visit', 'info', 'example', 'hash', 'tag']
        self.assertIsInstance(tokens, list)
        self.assertEqual(tokens, output_tokens)
