import unittest
from mongomock import MongoClient
from api.models.domain.reddit_post import RedditPost  # Importăm RedditPost din modulul corect
from api.repositories.general.comments_repository import CommentsRepository
from bson import ObjectId  # Necesită pentru ObjectId în testele MongoDB

class CommentsRepositoryTests(unittest.TestCase):
    def setUp(self):
        """
        Configurarea inițială pentru fiecare test.
        Creează o bază de date MongoDB simulată folosind mongomock.
        """
        self.client = MongoClient()  # Crează clientul simulant
        self.db = self.client["test_db"]  # Creează baza de date "test_db" pentru testare
        self.comments_repository = CommentsRepository(self.db)  # Instanțierea corectă a repo-ului
        
        # Creăm posturi simulate pentru testare
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
        
        # Comentarii simulate pentru testare
        self.mock_comments = [
            {"post_id": "123", "comment": "First comment", "user": "user1"},
            {"post_id": "123", "comment": "Second comment", "user": "user2"},
            {"post_id": "456", "comment": "Another comment", "user": "user3"}
        ]
    
    def test_get_comments_for_post(self):
        """
        Testează metoda get_comments_for_post pentru un post_id existent.
        """
        # Adăugăm posturile și comentariile simulate în colecția MongoDB
        self.db.reddit_posts.insert_many([post.__dict() for post in self.mock_posts])
        self.db.reddit_comments.insert_many(self.mock_comments)

        # Apelăm metoda
        result = self.comments_repository.get_comments_for_post("123")

        # Verificăm rezultatul
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["comment"], "First comment")
        self.assertEqual(result[1]["comment"], "Second comment")

    def test_get_comments_for_post_no_results(self):
        """
        Testează metoda get_comments_for_post pentru un post_id inexistent.
        """
        # Nu inserăm niciun comentariu pentru acest test
        result = self.comments_repository.get_comments_for_post("nonexistent_id")

        # Verificăm că lista returnată este goală
        self.assertEqual(result, [])

    def tearDown(self):
        """
        Eliberăm resursele după fiecare test.
        """
        # Nu este necesar să apelăm `self.client.close()` în cazul mongomock, dar dacă ai o conexiune reală ar trebui să o închizi
        self.client.close()  # Închidem conexiunea simulată pentru a evita problemele de memorie

if __name__ == "__main__":
    unittest.main()
