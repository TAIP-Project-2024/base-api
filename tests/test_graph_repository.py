import unittest
import os
from io import BytesIO
from unittest.mock import patch
from mongomock import MongoClient
from api.repositories.general.graph_repository import GraphRepository
from dotenv import load_dotenv
import logging

# Încarcă variabilele de mediu din fișierul .env
load_dotenv('.env')

# Obținem variabilele de mediu
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
LOCAL_GRAPHS_DIR = os.getenv("LOCAL_GRAPHS_DIR")

logging.basicConfig(level=logging.DEBUG)

class GraphRepositoryTests(unittest.TestCase):
    def setUp(self):
        """
        Configurarea inițială a testelor.
        Folosim MongoDB simulată și configurăm repository-ul pentru teste.
        """
        if not MONGO_DB_NAME:
            raise ValueError("MONGO_DB_NAME nu este setat corespunzător!")

        # Simulăm MongoDB cu mongomock
        self.client = MongoClient()
        self.db = self.client[MONGO_DB_NAME]
        self.fs = self.db["Graphs"]
        self.graph_repository = GraphRepository()

        # Creăm fișier mock pentru teste
        self.mock_graph_file = BytesIO(b"This is a mock graph file.")
        self.mock_graph_name = "test_graph"
        self.mock_graph_path = os.path.join(LOCAL_GRAPHS_DIR, self.mock_graph_name)

        # Asigurăm existența directorului local pentru grafuri
        os.makedirs(os.path.dirname(self.mock_graph_path), exist_ok=True)

        # Salvăm fișierul local
        with open(self.mock_graph_path, "wb") as f:
            f.write(self.mock_graph_file.getvalue())

    # def test_add_graph(self):
    #     """
    #     Testează adăugarea unui fișier grafic în MongoDB.
    #     """
    #     file_id = self.graph_repository.add(self.mock_graph_name, self.mock_graph_file)
    #     self.assertIsNotNone(file_id)

    #     file = self.db.fs.files.find_one({"filename": self.mock_graph_name})
    #     self.assertIsNotNone(file)
    #     self.assertEqual(file["filename"], self.mock_graph_name)

    #     logging.debug("Graph added with ID: %s", file_id)

    def test_get_graph(self):
        """
        Testează obținerea unui grafic stocat în MongoDB.
        """
        self.graph_repository.add(self.mock_graph_name, self.mock_graph_file)

        file_buffer = self.graph_repository.get(self.mock_graph_name)
        self.assertIsNotNone(file_buffer)

        file_buffer.seek(0)
        self.assertEqual(file_buffer.read(), b"This is a mock graph file.")

        logging.debug("Graph retrieved successfully: %s", self.mock_graph_name)

    def test_get_graph_not_found(self):
        """
        Testează cazul când un grafic nu este găsit.
        """
        result = self.graph_repository.get("nonexistent_graph")
        self.assertIsNone(result)
        logging.debug("Graph not found as expected: nonexistent_graph")

    def test_check_graph_exists(self):
        """
        Testează verificarea existenței unui fișier grafic.
        """
        self.graph_repository.add(self.mock_graph_name, self.mock_graph_file)

        exists = self.graph_repository.check_exists(self.mock_graph_name)
        self.assertTrue(exists)

        exists = self.graph_repository.check_exists("nonexistent_graph")
        self.assertFalse(exists)

        logging.debug("Graph existence check completed.")

    # def test_update_graph(self):
    #     """
    #     Testează actualizarea unui fișier grafic.
    #     """
    #     self.graph_repository.add(self.mock_graph_name, self.mock_graph_file)

    #     updated_graph_file = BytesIO(b"This is an updated mock graph file.")
    #     updated_file_id = self.graph_repository.update(self.mock_graph_name, updated_graph_file)

    #     self.assertIsNotNone(updated_file_id)

    #     file_buffer = self.graph_repository.get(self.mock_graph_name)
    #     self.assertIsNotNone(file_buffer)
    #     file_buffer.seek(0)
    #     self.assertEqual(file_buffer.read(), b"This is an updated mock graph file.")

    #     logging.debug("Graph updated successfully: %s", self.mock_graph_name)

    def test_delete_graph(self):
        """
        Testează ștergerea unui fișier grafic.
        """
        self.graph_repository.add(self.mock_graph_name, self.mock_graph_file)

        result = self.graph_repository.delete(self.mock_graph_name)
        self.assertTrue(result)

        file = self.db.fs.files.find_one({"filename": self.mock_graph_name})
        self.assertIsNone(file)

        result = self.graph_repository.delete("nonexistent_graph")
        self.assertFalse(result)

        logging.debug("Graph deletion completed.")

    def tearDown(self):
        """
        Eliberăm resursele după fiecare test.
        """
        self.client.drop_database(MONGO_DB_NAME)

        # Ștergem fișierul local dacă există
        if os.path.exists(self.mock_graph_path):
            os.remove(self.mock_graph_path)
            logging.debug("Local graph file removed: %s", self.mock_graph_path)


if __name__ == "__main__":
    unittest.main()
