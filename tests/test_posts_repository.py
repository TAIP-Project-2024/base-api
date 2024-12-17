import unittest
from bson import ObjectId
from mongomock import MongoClient
from api.models.domain.reddit_post import RedditPost
from api.repositories.general.posts_repository import PostsRepository


class TestPostsRepository(unittest.TestCase):

    def setUp(self):
        self.client = MongoClient()
        self.db = self.client["test_db"]
        self.posts_collection = self.db.posts
        self.posts_repository = PostsRepository(self.db)
        self.test_post_1 = {
            "_id": ObjectId(),
            "title": "post 1",
            "content": "content post 1"
        }
        self.test_post_2 = {
            "_id": ObjectId(),
            "title": "post 2",
            "content": "content post 2"
        }
        self.test_post_3 = {
            "_id": ObjectId(),
            "title": "post 3",
            "content": "content post 3"
        }
        self.posts_collection.insert_many([self.test_post_1, self.test_post_2, self.test_post_3])

    def test_get_all(self):
        posts = self.posts_repository.get_all()
        self.assertEqual(len(posts), 3)  
        self.assertEqual(posts[0].title, "post 1")
        self.assertEqual(posts[1].title, "post 2")
        self.assertEqual(posts[2].title, "post 3")

    def test_get_all_paginated(self):
        posts_page_1 = self.posts_repository.get_all_paginated(1, 2)
        self.assertEqual(len(posts_page_1), 2) 
        self.assertEqual(posts_page_1[0].title, "post 1")
        self.assertEqual(posts_page_1[1].title, "post 2")

        posts_page_2 = self.posts_repository.get_all_paginated(2, 2)
        self.assertEqual(len(posts_page_2), 1)  
        self.assertEqual(posts_page_2[0].title, "post 3")

    def test_get_by_id(self):
        post_id = self.test_post_1["_id"]
        post = self.posts_repository.get_by_id(post_id)
        self.assertIsNotNone(post)
        self.assertEqual(post["_id"], post_id)
        self.assertEqual(post["title"], "post 1")

    def tearDown(self):
        self.client.drop_database("test_db")


if __name__ == "__main__":
    unittest.main()
