import unittest
from io import BytesIO
from mongomock import MongoClient
from unittest.mock import MagicMock, patch
from api.repositories.general.graph_repository import GraphRepository
import logging

logging.basicConfig(level=logging.DEBUG)


class GraphRepositoryTests(unittest.TestCase):
    def setUp(self):
        """
        Set up a mock MongoDB instance and GraphRepository for testing.
        """
        # Mock MongoDB setup
        self.client = MongoClient()
        self.db = self.client["test_database"]

        # Patch GridFS to avoid incompatibilities
        self.gridfs_mock = MagicMock()
        self.fs_patch = patch("gridfs.GridFS", return_value=self.gridfs_mock)
        self.fs_patch.start()

        # Mock the repository
        self.graph_repository = GraphRepository()
        self.graph_repository.client = self.client
        self.graph_repository.db = self.db
        self.graph_repository.fs = self.gridfs_mock

        # Test graph file setup
        self.mock_graph_name = "test_graph"
        self.mock_graph_file = BytesIO(b"This is a mock graph file.")

    def test_add_graph(self):
        """
        Test the add method of GraphRepository.
        """
        file_id = self.graph_repository.add(self.mock_graph_name, self.mock_graph_file)
        self.assertIsNotNone(file_id)

        # Assert that the put method was called
        self.gridfs_mock.put.assert_called_once_with(self.mock_graph_file, filename=self.mock_graph_name)
        logging.debug("Graph added successfully.")

    def test_get_graph(self):
        """
        Test the get method of GraphRepository.
        """
        # Mock the return value for the find_one method
        mock_file = MagicMock()
        mock_file.read.return_value = b"This is a mock graph file."
        self.gridfs_mock.find_one.return_value = mock_file

        file_buffer = self.graph_repository.get(self.mock_graph_name)
        self.assertIsNotNone(file_buffer)
        file_buffer.seek(0)
        self.assertEqual(file_buffer.read(), b"This is a mock graph file.")
        logging.debug("Graph retrieved successfully.")

    def test_get_graph_not_found(self):
        """
        Test get method for a non-existing graph.
        """
        self.gridfs_mock.find_one.return_value = None
        file_buffer = self.graph_repository.get("nonexistent_graph")
        self.assertIsNone(file_buffer)
        logging.debug("Nonexistent graph retrieval returned None as expected.")

    def test_check_graph_exists(self):
        """
        Test the check_exists method of GraphRepository.
        """
        # Mock the return value for exists
        self.gridfs_mock.exists.side_effect = lambda query: query.get("filename") == self.mock_graph_name

        exists = self.graph_repository.check_exists(self.mock_graph_name)
        self.assertTrue(exists)

        nonexistent = self.graph_repository.check_exists("nonexistent_graph")
        self.assertFalse(nonexistent)
        logging.debug("Graph existence checks completed.")

    def test_update_graph(self):
        """
        Test the update method of GraphRepository.
        """
        # Mock the existing file to simulate replacement
        mock_file = MagicMock()
        mock_file._id = "mock_file_id"
        self.gridfs_mock.find_one.return_value = mock_file

        updated_file = BytesIO(b"This is an updated mock graph file.")
        file_id = self.graph_repository.update(self.mock_graph_name, updated_file)
        self.assertIsNotNone(file_id)

        # Assert the delete and put methods were called
        self.gridfs_mock.delete.assert_called_once_with("mock_file_id")
        self.gridfs_mock.put.assert_called_once_with(updated_file, filename=self.mock_graph_name)
        logging.debug("Graph updated successfully.")

    def test_delete_graph(self):
        """
        Test the delete method of GraphRepository.
        """
        # Mock the existing file to simulate deletion
        mock_file = MagicMock()
        mock_file._id = "mock_file_id"
        self.gridfs_mock.find_one.return_value = mock_file

        deleted = self.graph_repository.delete(self.mock_graph_name)
        self.assertTrue(deleted)

        # Assert that delete was called
        self.gridfs_mock.delete.assert_called_once_with("mock_file_id")

        # Test deletion of nonexistent file
        self.gridfs_mock.find_one.return_value = None
        deleted_nonexistent = self.graph_repository.delete("nonexistent_graph")
        self.assertFalse(deleted_nonexistent)
        logging.debug("Graph deletion tests completed.")

    def tearDown(self):
        """
        Clean up resources after each test.
        """
        self.fs_patch.stop()
        self.client.drop_database("test_database")
        logging.debug("Mock database cleaned up.")


if __name__ == "__main__":
    unittest.main()
