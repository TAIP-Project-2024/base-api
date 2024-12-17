import unittest
from io import BytesIO
from unittest.mock import patch
from mongomock import MongoClient
from api.repositories.general.graph_drawing_repository import DrawingRepository
import logging

logging.basicConfig(level=logging.DEBUG)

class DrawingRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient()

        self.db = self.client["test_db"] 
        self.fs = self.db["Drawings"]
        self.drawing_repository = DrawingRepository()

        self.mock_drawing_file = BytesIO(b"This is a mock drawing file.")
        self.mock_drawing_name = "test_drawing"

    def test_add_drawing(self):
        file_id = self.drawing_repository.add(self.mock_drawing_name, self.mock_drawing_file)

        file = self.fs.find_one({"filename": self.mock_drawing_name})
        self.assertIsNotNone(file)
        self.assertEqual(file.filename, self.mock_drawing_name)
        self.assertEqual(file_id, file._id)

        logging.debug("File added to DB, file ID: %s", file_id)
        logging.debug("File retrieved: %s", file)

    def test_get_drawing(self):
        self.drawing_repository.add(self.mock_drawing_name, self.mock_drawing_file)

        file_buffer = self.drawing_repository.get(self.mock_drawing_name)

        self.assertIsNotNone(file_buffer)
        file_buffer.seek(0)
        self.assertEqual(file_buffer.read(), b"This is a mock drawing file.")

        logging.debug("Retrieved file: %s", file_buffer)

    def test_get_drawing_not_found(self):
        result = self.drawing_repository.get("nonexistent_drawing")
        self.assertIsNone(result)
        logging.debug("No drawing found for 'nonexistent_drawing': %s", result)

    def test_check_drawing_exists(self):
        self.drawing_repository.add(self.mock_drawing_name, self.mock_drawing_file)

        exists = self.drawing_repository.check_exists(self.mock_drawing_name)
        self.assertTrue(exists)

        exists = self.drawing_repository.check_exists("nonexistent_drawing")
        self.assertFalse(exists)

        logging.debug("Drawing exists: %s", exists)

    def test_update_drawing(self):
        self.drawing_repository.add(self.mock_drawing_name, self.mock_drawing_file)

        updated_drawing_file = BytesIO(b"This is an updated mock drawing file.")
        
        updated_file_id = self.drawing_repository.update(self.mock_drawing_name, updated_drawing_file)

        file = self.fs.find_one({"filename": self.mock_drawing_name})
        self.assertIsNotNone(file)
        self.assertEqual(file.filename, self.mock_drawing_name)
        self.assertEqual(updated_file_id, file._id)

        old_file = self.fs.find_one({"filename": self.mock_drawing_name})
        self.assertIsNone(old_file)

        logging.debug("Updated file ID: %s", updated_file_id)
        logging.debug("Original file deleted: %s", old_file)

    def test_delete_drawing(self):
        self.drawing_repository.add(self.mock_drawing_name, self.mock_drawing_file)

        result = self.drawing_repository.delete(self.mock_drawing_name)

        self.assertTrue(result)
        file = self.fs.find_one({"filename": self.mock_drawing_name})
        self.assertIsNone(file)

        result = self.drawing_repository.delete("nonexistent_drawing")
        self.assertFalse(result)

        logging.debug("Delete result for existing drawing: %s", result)
        logging.debug("Delete result for nonexistent drawing: %s", result)

    def tearDown(self):
        self.client.close()


if __name__ == "__main__":
    unittest.main()
