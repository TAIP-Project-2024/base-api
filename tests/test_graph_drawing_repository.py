import unittest
from unittest.mock import MagicMock, patch
from io import BytesIO

from api.repositories.general.graph_drawing_repository import DrawingRepository


class DrawingRepositoryTests(unittest.TestCase):
    def setUp(self):
        # Mock the MongoClient, GridFS, and dependencies
        patcher_mongo = patch("api.repositories.general.graph_drawing_repository.MongoClient")
        patcher_gridfs = patch("api.repositories.general.graph_drawing_repository.GridFS")

        self.mock_mongo_client = patcher_mongo.start()
        self.mock_gridfs = patcher_gridfs.start()

        self.addCleanup(patcher_mongo.stop)
        self.addCleanup(patcher_gridfs.stop)

        self.mock_fs = MagicMock()
        self.mock_gridfs.return_value = self.mock_fs
        self.mock_db = self.mock_mongo_client.return_value["mock_db"]

        # Instantiate the repository
        self.repo = DrawingRepository()

    def tearDown(self):
        self.repo.close()

    def test_add_drawing(self):
        # Arrange
        mock_file_buffer = BytesIO(b"mock content")
        mock_file_id = "mock_file_id"
        self.mock_fs.put.return_value = mock_file_id

        # Act
        result = self.repo.add("TestDrawing", mock_file_buffer)

        # Assert
        self.mock_fs.put.assert_called_once_with(mock_file_buffer, filename="TestDrawing")
        self.assertEqual(result, mock_file_id)

    def test_get_existing_drawing(self):
        # Arrange
        mock_file_content = b"mock content"
        mock_file = MagicMock()
        mock_file.read.return_value = mock_file_content
        self.mock_fs.find_one.return_value = mock_file

        # Act
        result = self.repo.get("TestDrawing")

        # Assert
        self.mock_fs.find_one.assert_called_once_with({"filename": "TestDrawing"})
        self.assertIsInstance(result, BytesIO)
        self.assertEqual(result.read(), mock_file_content)

    def test_get_non_existing_drawing(self):
        # Arrange
        self.mock_fs.find_one.return_value = None

        # Act
        result = self.repo.get("NonExistentDrawing")

        # Assert
        self.mock_fs.find_one.assert_called_once_with({"filename": "NonExistentDrawing"})
        self.assertIsNone(result)

    def test_check_exists(self):
        # Arrange
        self.mock_fs.exists.return_value = True

        # Act
        result = self.repo.check_exists("ExistingDrawing")

        # Assert
        self.mock_fs.exists.assert_called_once_with({"filename": "ExistingDrawing"})
        self.assertTrue(result)

    def test_update_existing_drawing(self):
        # Arrange
        mock_file_buffer = BytesIO(b"updated content")
        mock_file_id = "updated_file_id"
        mock_existing_file = MagicMock()
        mock_existing_file._id = "existing_file_id"
        self.mock_fs.find_one.return_value = mock_existing_file
        self.mock_fs.put.return_value = mock_file_id

        # Act
        result = self.repo.update("TestDrawing", mock_file_buffer)

        # Assert
        self.mock_fs.find_one.assert_called_once_with({"filename": "TestDrawing"})
        self.mock_fs.delete.assert_called_once_with("existing_file_id")
        self.mock_fs.put.assert_called_once_with(mock_file_buffer, filename="TestDrawing")
        self.assertEqual(result, mock_file_id)

    def test_update_non_existing_drawing(self):
        # Arrange
        mock_file_buffer = BytesIO(b"new content")
        mock_file_id = "new_file_id"
        self.mock_fs.find_one.return_value = None
        self.mock_fs.put.return_value = mock_file_id

        # Act
        result = self.repo.update("NewDrawing", mock_file_buffer)

        # Assert
        self.mock_fs.find_one.assert_called_once_with({"filename": "NewDrawing"})
        self.mock_fs.put.assert_called_once_with(mock_file_buffer, filename="NewDrawing")
        self.assertEqual(result, mock_file_id)

    def test_delete_existing_drawing(self):
        # Arrange
        mock_existing_file = MagicMock()
        mock_existing_file._id = "existing_file_id"
        self.mock_fs.find_one.return_value = mock_existing_file

        # Act
        result = self.repo.delete("TestDrawing")

        # Assert
        self.mock_fs.find_one.assert_called_once_with({"filename": "TestDrawing"})
        self.mock_fs.delete.assert_called_once_with("existing_file_id")
        self.assertTrue(result)

    def test_delete_non_existing_drawing(self):
        # Arrange
        self.mock_fs.find_one.return_value = None

        # Act
        result = self.repo.delete("NonExistentDrawing")

        # Assert
        self.mock_fs.find_one.assert_called_once_with({"filename": "NonExistentDrawing"})
        self.mock_fs.delete.assert_not_called()
        self.assertFalse(result)

    def test_close(self):
        # Act
        self.repo.close()

        # Assert
        self.mock_mongo_client.return_value.close.assert_called_once()

    def test_context_manager(self):
        # Test the context manager functionality
        with DrawingRepository() as repo:
            self.assertIsInstance(repo, DrawingRepository)
        self.mock_mongo_client.return_value.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
