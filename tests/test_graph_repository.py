import os
import unittest
from io import BytesIO
from unittest.mock import patch
from mongomock import MongoClient
from api.repositories.general.graph_repository import GraphRepository
from dotenv import load_dotenv

load_dotenv('.env')

class GraphRepositoryTests(unittest.TestCase):
    
    def setUp(self):
        os.environ["MONGO_DB_NAME"] = "test_graph_db"  
        os.environ["MONGO_URI"] = "mongodb://localhost:27017" 
        self.client = MongoClient()
        self.db = self.client["test_graph_db"]  
        self.fs = self.db["Graphs"]

        self.graph_repository = GraphRepository()
        self.mock_graph_file = BytesIO(b"This is a mock graph file.")
        self.mock_graph_name = "test_graph"

    def test_add_graph(self):
        file_id = self.graph_repository.add(self.mock_graph_name, self.mock_graph_file)
        self.assertIsNotNone(file_id)
        file = self.fs.find_one({"filename": self.mock_graph_name})
        self.assertIsNotNone(file)
        self.assertEqual(file.filename, self.mock_graph_name)

    def test_get_graph(self):
        self.graph_repository.add(self.mock_graph_name, self.mock_graph_file)
        result = self.graph_repository.get(self.mock_graph_name)
        self.assertIsInstance(result, BytesIO)
        self.assertEqual(result.getvalue(), b"This is a mock graph file.")

    def test_get_graph_not_found(self):
        result = self.graph_repository.get("nonexistent_graph")
        self.assertIsNone(result)

    def test_check_graph_exists(self):
        self.graph_repository.add(self.mock_graph_name, self.mock_graph_file)
        exists = self.graph_repository.check_exists(self.mock_graph_name)
        self.assertTrue(exists)

        exists = self.graph_repository.check_exists("nonexistent_graph")
        self.assertFalse(exists)

    def test_update_graph(self):
        self.graph_repository.add(self.mock_graph_name, self.mock_graph_file)
        updated_file = BytesIO(b"This is an updated mock graph file.")
        file_id = self.graph_repository.update(self.mock_graph_name, updated_file)
        self.assertIsNotNone(file_id)
    
        file = self.fs.find_one({"filename": self.mock_graph_name})
        self.assertIsNotNone(file)
        self.assertEqual(file.filename, self.mock_graph_name)
        result = self.graph_repository.get(self.mock_graph_name)
        self.assertEqual(result.getvalue(), b"This is an updated mock graph file.")

    def test_delete_graph(self):
        self.graph_repository.add(self.mock_graph_name, self.mock_graph_file)
        deleted = self.graph_repository.delete(self.mock_graph_name)
        self.assertTrue(deleted)
        
        file = self.fs.find_one({"filename": self.mock_graph_name})
        self.assertIsNone(file)

    def test_delete_graph_not_found(self):
        deleted = self.graph_repository.delete("nonexistent_graph")
        self.assertFalse(deleted)

    def tearDown(self):
        self.client.drop_database("test_graph_db")

if __name__ == "__main__":
    unittest.main()
