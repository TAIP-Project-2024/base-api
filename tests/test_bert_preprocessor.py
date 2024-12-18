import unittest

from api.ml_core.data_preprocess.bert_preprocessor import BertPreprocessor


class BertPreprocessorTest(unittest.TestCase):
    def setUp(self):
        self.preprocessor = BertPreprocessor()

    def test_preprocess_bert_equal(self):
        input_text = "u/Trump http www r/politics"
        output_text = "@user http www subreddit"
        self.assertEqual(self.preprocessor.preprocess_bert(input_text), output_text)

    def test_preprocess_bert_not_equal(self):
        input_text = "u/Trump http www r/politics"
        output_text = "@user http www r/politics"
        self.assertNotEqual(self.preprocessor.preprocess_bert(input_text), output_text)

    def test_preprocess_equal(self):
        input_text = "u/Trump http www r/politics"
        output_text = "@user http www subreddit"
        self.assertEqual(self.preprocessor.preprocess(input_text), output_text)

    def test_preprocess_not_equal(self):
        input_text = "u/Trump http www r/politics"
        output_text = "@user http www r/politics"
        self.assertNotEqual(self.preprocessor.preprocess(input_text), output_text)
