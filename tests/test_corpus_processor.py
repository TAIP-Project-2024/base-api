import unittest

from api.ml_core.data_preprocess.corpus_processor import CorpusProcessor


class CorpusProcessorTest(unittest.TestCase):
    def test_bigrams_trigrams(self):
        data = [["natural", "language", "processing", "is", "fun"],
                ["natural", "language", "is", "powerful"],
                ["I", "study", "natural", "language"],
                ["Something", "about", "natural", "language"],
                ["Another", "list", "with", "natural", "language"],
                ["natural", "language", "is", "cool"]]
        result = CorpusProcessor.bigrams_trigrams(data, min_count=2, threshold=2)
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(doc, list) for doc in result))

        self.assertIn("natural_language", result[0])

    def test_remove_frequent_words(self):
        data_trigram = [["data", "analysis", "is", "useful"], ["data", "is", "important"]]

        corpus, id2word = CorpusProcessor.remove_frequent_words(data_trigram)

        self.assertIsNotNone(corpus)
        self.assertIsNotNone(id2word)

        frequent_words = ["data"]
        for doc in corpus:
            for word_id, _ in doc:
                self.assertNotIn(id2word[word_id], frequent_words)
