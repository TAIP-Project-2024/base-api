import unittest

from api.ml_core.data_preprocess.sentiment_analysis_preprocessor import SentimentAnalysisPreprocessor
from api.ml_core.data_preprocess.text_preprocessor import TextPreprocessor


class TopicModelingPreprocessorTest(unittest.TestCase):
    def setUp(self):
        self.preprocessor = SentimentAnalysisPreprocessor()

    def test_init(self):
        self.assertIsNotNone(self.preprocessor)

    def test_text_preprocess(self):
        with self.assertRaises(TypeError):
            preprocess = TextPreprocessor()
            preprocess.preprocess("This is a test")

    def test_preprocess(self):
        input_text = "This is a test"
        output_text = ['this', 'is', 'a', 'test']
        self.assertEqual(self.preprocessor.preprocess(input_text), output_text)

    def test_lowercase_equal(self):
        input_text = "This is a TEST"
        output_text = "this is a test"
        self.assertEqual(self.preprocessor.lowercase(input_text), output_text)

    def test_lowercase_not_equal(self):
        input_text = "This is a TEST"
        output_text = "This is a TEST"
        self.assertNotEqual(self.preprocessor.lowercase(input_text), output_text)

    def test_remove_urls_equal(self):
        input_text = "This is a URL: https://example.com"
        output_text = "This is a URL:  "
        self.assertEqual(self.preprocessor.remove_urls(input_text), output_text)

    def test_remove_urls_not_equal(self):
        input_text = "This is a URL: https://example.com"
        output_text = "This is a URL: https://example.com"
        self.assertNotEqual(self.preprocessor.remove_urls(input_text), output_text)

    def test_remove_mentions_equal(self):
        input_text = "This is a mention: u/username . This is a mention: r/subreddit"
        output_text = "This is a mention:   . This is a mention:  "
        self.assertEqual(self.preprocessor.remove_mentions(input_text), output_text)

    def test_remove_mentions_not_equal(self):
        input_text = "This is a mention: u/username . This is a mention: r/subreddit"
        output_text = "This is a mention: u/username . This is a mention: r/subreddit"
        self.assertNotEqual(self.preprocessor.remove_mentions(input_text), output_text)

    def test_hashtag_extraction_equal(self):
        input_text = "text with a #hashtag"
        output_text = "text with a hash tag"
        self.assertEqual(self.preprocessor.hashtag_extraction(input_text), output_text)

    def test_hashtag_extraction_not_equal(self):
        input_text = "text with a #hashtag"
        output_text = "text with a #hashtag"
        self.assertNotEqual(self.preprocessor.hashtag_extraction(input_text), output_text)

    def test_expand_contractions_equal(self):
        input_text = "This can't be a test"
        output_text = "This cannot be a test"
        self.assertEqual(self.preprocessor.expand_contractions(input_text), output_text)

    def test_expand_contractions_not_equal(self):
        input_text = "This can't be a test"
        output_text = "This can't be a test"
        self.assertNotEqual(self.preprocessor.expand_contractions(input_text), output_text)

    def test_lemmatize_text(self):
        input_text = "This is a test"
        output_text = "this be a test"
        self.assertEqual(self.preprocessor.lemmatize_text(input_text), output_text)

    def test_lemmatize_text_not_equal(self):
        input_text = "This is a test"
        output_text = "This is a test"
        self.assertNotEqual(self.preprocessor.lemmatize_text(input_text), output_text)

    def test_lemmatize_with_allowed_postags(self):
        input_text = "This is a test"
        output_text = "test"
        allowed_postags = ["VERB", "NOUN"]
        self.assertEqual(
            self.preprocessor.lemmatize_text(input_text, allowed_postags=allowed_postags),
            output_text
        )

    def test_empty_input(self):
        self.assertEqual(self.preprocessor.lowercase(""), "")
        self.assertEqual(self.preprocessor.remove_urls(""), "")
        self.assertEqual(self.preprocessor.remove_mentions(""), "")
        self.assertEqual(self.preprocessor.hashtag_extraction(""), "")
        self.assertEqual(self.preprocessor.expand_contractions(""), "")
        self.assertEqual(self.preprocessor.lemmatize_text(""), "")
