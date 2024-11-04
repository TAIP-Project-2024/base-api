from django.test import TestCase
from api.repositories.general.posts_repository import PostsRepository
import unittest
from mongomock import MongoClient


class PostsRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient()
        self.posts_repository = PostsRepository("test_db")
        self.db = self.client["test_db"]

    def test_get_all(self):
        self.db.posts.insert_one({"title": "test", "content": "test"})
        self.assertEqual(self.posts_repository.get_all(), [{"title": "test", "content": "test"}])

    def test_get_by_id(self):
        self.db.posts.insert_one({"title": "test", "content": "test"})
        self.assertEqual(self.posts_repository.get_by_id(1), {"title": "test", "content": "test"})

    def test_get_all_paginated(self):
        self.db.posts.insert_one({"title": "test", "content": "test"})
        self.assertEqual(self.posts_repository.get_all_paginated(1, 1), [{"title": "test", "content": "test"}])

