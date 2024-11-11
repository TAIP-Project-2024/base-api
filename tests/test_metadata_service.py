import unittest
from importlib.metadata import metadata

from api.services.general.metadata_service import MetadataService


class TestMetadataService(unittest.TestCase):
    def setUp(self):
        self.author = "AuthorName"
        self.post = "This is a sample post."
        self.reactions = [{"user": "user1", "comment": "I like it!", "sentiment": 0.7},
                          {"user": "user2", "comment": "I like it a bit!", "sentiment": 0.6},
                          {"user": "user3", "comment": "I used to like it", "sentiment": 0.5},
                          {"user": "user4", "comment": "I hardly like it!", "sentiment": 0.4},
                          {"user": "user5", "comment": "I like smth else!", "sentiment": 0.3},
                          {"user": "user6", "comment": "I don't like it!", "sentiment": 0.2},
                          {"user": "user7", "comment": "I'm against!", "sentiment": 0.1},
                          {"user": "user8", "comment": "I hate it!", "sentiment": 0.0}]

    def test_generate_metadata(self):
        metadata = MetadataService.generate_metadata_for_post(
            author=self.author,
            post=self.post,
            reactions=self.reactions
        )

        self.assertIsInstance(metadata, dict)

        self.assertIn("author", metadata)
        self.assertIn("post", metadata)
        self.assertIn("reactions", metadata)

        self.assertEqual(metadata["author"], self.author)
        self.assertEqual(metadata["post"], self.post)
        self.assertEqual(metadata["reactions"], self.reactions)