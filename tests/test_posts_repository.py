from api.models.domain.reddit_post import RedditPost
from api.repositories.general.posts_repository import PostsRepository
import unittest
from mongomock import MongoClient


class PostsRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient()
        self.db = self.client["test_db"]
        self.posts_repository = PostsRepository(self.db)
        self.mock_reddit_post = RedditPost("test", "test", "test", "test", "test", "test", "test", "test", "test")

    def test_get_all(self):
        self.db.posts.insert_one(self.mock_reddit_post.__dict__())
        self.assertEqual(self.posts_repository.get_all(), [self.mock_reddit_post])

    def test_get_by_id(self):
        self.db.posts.insert_one(self.mock_reddit_post.__dict__())
        result = RedditPost.from_dict(self.posts_repository.get_by_id(self.mock_reddit_post._id))
        self.assertEqual(result, self.mock_reddit_post)

    def test_get_all_paginated(self):
        self.db.posts.insert_one(self.mock_reddit_post.__dict__())
        self.assertEqual(self.posts_repository.get_all_paginated(1, 1), [self.mock_reddit_post])

