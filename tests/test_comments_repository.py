import unittest
from mongomock import MongoClient
from api.models.domain.reddit_post import RedditPost  
from api.repositories.general.comments_repository import CommentsRepository
from bson import ObjectId  

class CommentsRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient() 
        self.db = self.client["test_db"]  
        self.comments_repository = CommentsRepository()
        self.comments_repository.client = self.client
        self.comments_repository.db = self.db
        self.comments_repository.collection = self.db["reddit_comments"]
        
        self.mock_posts = [
            RedditPost(
                title="Post 1", content="Content 1", text="Text 1", subreddit="sub1",
                created_at="2024-12-17", score=100, num_comments=2, is_self=True,
                url="http://example.com", post_id="123"
            ),
            RedditPost(
                title="Post 2", content="Content 2", text="Text 2", subreddit="sub2",
                created_at="2024-12-17", score=50, num_comments=1, is_self=False,
                url="http://example.com", post_id="456"
            ),
        ]
        
        self.mock_comments = [
            {"post_id": "123", "comment": "First comment", "user": "user1"},
            {"post_id": "123", "comment": "Second comment", "user": "user2"},
            {"post_id": "456", "comment": "Another comment", "user": "user3"}
        ]
    
    def test_get_comments_for_post(self):
        self.db.reddit_posts.insert_many([post.__dict__() for post in self.mock_posts])
        self.db.reddit_comments.insert_many(self.mock_comments)

        result = self.comments_repository.get_comments_for_post("123")

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["comment"], "First comment")
        self.assertEqual(result[1]["comment"], "Second comment")

    def test_get_comments_for_post_no_results(self):
        result = self.comments_repository.get_comments_for_post("nonexistent_id")

        self.assertEqual(result, [])

    def tearDown(self):
        self.client.close()  

if __name__ == "__main__":
    unittest.main()
