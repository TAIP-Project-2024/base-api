import shutil
import tempfile
import unittest
from unittest.mock import patch, MagicMock

import gensim

from api.ml_core.topic_modeling.lda_model import LDAModel


class LDAModelTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()  # Temporary directory for model
        self.lda_model = LDAModel()
        self.lda_model.model_filename = tempfile.mktemp(dir=self.temp_dir)

        self.test_data = [
            "The economy is struggling to inflation",
            "Rising prices are impacting our citizens"
        ]

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_set_num_topics(self):
        self.lda_model.set_num_topics(10)
        self.assertEqual(self.lda_model.num_topics, 10)

    def test_set_alpha(self):
        self.lda_model.set_alpha(0.5)
        self.assertEqual(self.lda_model.alpha, 0.5)

    def test_set_beta(self):
        self.lda_model.set_beta(0.5)
        self.assertEqual(self.lda_model.beta, 0.5)

    def test_train_new_model(self):
        model, corpus, id2word = self.lda_model.train(self.test_data)
        self.assertIsInstance(model, gensim.models.ldamodel.LdaModel)
        self.assertIsNotNone(corpus)
        self.assertIsInstance(id2word, gensim.corpora.Dictionary)

    @patch("gensim.corpora.Dictionary.load")
    @patch("gensim.models.ldamodel.LdaModel.load")
    @patch("os.path.exists")
    def test_train_existing_model(self, mock_exists, mock_load, mock_dict_load):
        mock_exists.return_value = True  # Simulates the model file exists
        mock_load.return_value = MagicMock(spec=gensim.models.LdaModel)  # Mock Loading the existing model
        mock_dict_load.return_value = MagicMock(spec=gensim.corpora.Dictionary)  # Mock loading the id2word dictionary

        model, corpus, id2word = self.lda_model.train(self.test_data)

        # Check if they exist and are called
        mock_exists.assert_any_call(self.lda_model.model_filename)
        mock_exists.assert_any_call(self.lda_model.model_filename + ".id2word")

        # Check if they are loaded
        mock_load.assert_called_with(self.lda_model.model_filename)
        mock_dict_load.assert_called_with(self.lda_model.model_filename + ".id2word")

        self.assertIsInstance(model, gensim.models.ldamodel.LdaModel)
        self.assertIsNone(corpus)
        self.assertIsNotNone(id2word)

    @patch("gensim.corpora.Dictionary.load")
    @patch("gensim.models.ldamodel.LdaModel.load")
    @patch("os.path.exists")
    def test_train_existing_model_exception_no_dictionary(self, mock_exists, mock_load, mock_dict_load):
        mock_exists.side_effect = [True, False] # exists model file, but no dictionary file
        mock_load.return_value = MagicMock(spec=gensim.models.LdaModel)  # Mock Loading the existing model
        mock_dict_load.side_effect = FileNotFoundError(
            "Dictionary file not found!")  # Mock loading the id2word dictionary

        with self.assertRaises(FileNotFoundError):
            self.lda_model.train(self.test_data)

        # Check if they exist and are called
        mock_exists.assert_any_call(self.lda_model.model_filename)
        mock_exists.assert_any_call(self.lda_model.model_filename + ".id2word")

        # Check if they are loaded
        mock_load.assert_called_with(self.lda_model.model_filename)

    def test_get_topics(self):
        model, corpus, id2word = self.lda_model.train(self.test_data)
        topics = self.lda_model.get_topics(model)
        self.assertEqual(len(topics), self.lda_model.num_topics)
        self.assertTrue(all(isinstance(topic, tuple) for topic in topics))

    def test_analyze(self):
        model, corpus, id2word = self.lda_model.train(self.test_data)
        result = self.lda_model.analyze(self.test_data[0])
        self.assertTrue(all(isinstance(topic, tuple) for topic in result))
        self.assertTrue(all(0 <= prob <= 1 for _, prob in result))


if __name__ == '__main__':
    unittest.main()
