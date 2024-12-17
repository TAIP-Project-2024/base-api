import unittest

from api.ml_core.utils.resource_manager import ResourceManager


class ResourceManagerTest(unittest.TestCase):
    def setUp(self):
        self.resource_manager = ResourceManager()

    def test_singleton_instance(self):
        resource_manager_2 = ResourceManager()
        self.assertEqual(self.resource_manager, resource_manager_2)

    def test_stop_words(self):
        self.assertIsInstance(self.resource_manager.stop_words, set)
        self.assertTrue(len(self.resource_manager.stop_words) > 0)

    def test_spacy_model(self):
        self.assertIsNotNone(self.resource_manager.spacy_model)

    def test_wordnet_map(self):
        self.assertIsInstance(self.resource_manager.wordnet_map, dict)
        self.assertTrue(len(self.resource_manager.wordnet_map) > 0)