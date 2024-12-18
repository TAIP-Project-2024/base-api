import unittest

from api.ml_core.topic_modeling.topic_model_interface import TopicModelInterface


class TopicModelInterfaceTest(unittest.TestCase):
    def test_analyze(self):
        topic_model_interface = TopicModelInterface()
        with self.assertRaises(NotImplementedError):
            topic_model_interface.analyze("This is a test")