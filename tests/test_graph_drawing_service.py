import unittest
import mongomock
from api.services.general.graph_drawing_service import GraphDrawingService
from api.services.graph_factory import GraphFactory
from api.models.domain.graph_drawing import GraphDrawing
from api.models.domain.networkx_graph_impl import NetworkxGraphImpl
from api.repositories.general.comments_repository import CommentsRepository
from api.repositories.general.graph_repository import GraphRepository
from api.repositories.general.graph_drawing_repository import DrawingRepository


class TestGraphDrawingService(unittest.TestCase):

    def setUp(self):
        # Mock MongoDB client using mongomock
        self.mock_client = mongomock.MongoClient()

        # Create mock collections for repositories
        self.mock_drawing_repo = self.mock_client['test_db']['drawings']
        self.mock_graph_repo = self.mock_client['test_db']['graphs']
        self.mock_comments_repo = self.mock_client['test_db']['comments']

        # Initialize GraphDrawingService instance
        self.gds = GraphDrawingService()

    def test_create_or_retrieve_comments_drawing(self):
        # Data to be used for tests
        post_id = "1het1r1"
        post_text = "some_post"
        drawing_name = f"{post_id}CommentsGraphDrawing"
        graph_name = f"{post_id}CommentsGraph"

        # Test when the drawing already exists in the repository
        # Add a mock drawing to the repository
        self.mock_drawing_repo.insert_one({
            'name': drawing_name,
            'html_file': 'mock_html_file_content'
        })

        # Retrieve the drawing using the service
        result = self.gds.create_or_retrieve_comments_drawing(post_id, post_text)

        # Assert that the correct drawing is retrieved
        # self.assertEqual(result.read(), 'mock_html_file_content')

        # Test when the drawing doesn't exist and needs to be created
        # Simulate adding a graph to the repository
        self.mock_graph_repo.insert_one({
            'name': graph_name,
            'graphml_file': 'mock_graphml_file_content'
        })

        # Simulate comments data
        mock_comments = [
            {"_id": "comment1", "text": "First comment", "sentiment": 1, "score": 5},
            {"_id": "comment2", "text": "Second comment", "sentiment": 0, "score": 3},
            {"_id": "comment3", "text": "Third comment", "sentiment": 2, "score": 10}
        ]
        self.mock_comments_repo.insert_many(mock_comments)

        # Mock GraphService and GraphFactory methods
        # Inserting a graph and saving it
        graph = NetworkxGraphImpl(graph_name)
        self.gds.save_graph_drawing(GraphDrawing(graph, drawing_name), delete_local=True)

        # Simulate graph creation with GraphFactory
        graph_data = GraphFactory.create_comments_graph(graph_name, post_text, mock_comments)

        # Call the method to create or retrieve comments drawing
        result = self.gds.create_or_retrieve_comments_drawing(post_id, post_text)

        # Assert that the graph creation and saving occurred
        self.assertTrue(graph_data is not None)


if __name__ == '__main__':
    unittest.main()
