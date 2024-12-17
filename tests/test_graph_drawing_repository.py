import unittest
import os
from io import BytesIO
from unittest.mock import patch
from mongomock import MongoClient
from api.repositories.general.graph_drawing_repository import DrawingRepository
from dotenv import load_dotenv

# Încarcă variabilele de mediu din fișierul .env
load_dotenv('.env')

# Obținem variabilele de mediu
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
LOCAL_GRAPHS_DIR = os.getenv("LOCAL_GRAPHS_DIR")

import logging

logging.basicConfig(level=logging.DEBUG)


class DrawingRepositoryTests(unittest.TestCase):
    def setUp(self):
        """
        Configurarea inițială a testelor.
        Folosim MongoDB simulant pentru a testa repository-ul.
        """
        if not MONGO_DB_NAME:
            raise ValueError("MONGO_DB_NAME nu este setat corespunzător!")

        # Folosim mongomock pentru a simula o bază de date MongoDB
        self.client = MongoClient()
        self.db = self.client[MONGO_DB_NAME]  # Numele bazei de date configurat în fișierul .env
        self.fs = self.db["Drawings"]
        self.drawing_repository = DrawingRepository()

        # Creăm un fișier mock de desen pentru testare
        self.mock_drawing_file = BytesIO(b"This is a mock drawing file.")
        self.mock_drawing_name = "test_drawing"
        self.mock_drawing_path = os.path.join(LOCAL_GRAPHS_DIR, self.mock_drawing_name)

        # Asigurăm că directorul există
        os.makedirs(os.path.dirname(self.mock_drawing_path), exist_ok=True)

        # Salvăm fișierul local
        with open(self.mock_drawing_path, "wb") as f:
            f.write(self.mock_drawing_file.getvalue())

    # def test_add_drawing(self):
    #     """
    #     Testează adăugarea unui desen în colecția MongoDB și în fișierele locale.
    #     """
    #     file_id = self.drawing_repository.add(self.mock_drawing_name, self.mock_drawing_file)

    #     file = self.fs.find_one({"filename": self.mock_drawing_name})
    #     self.assertIsNotNone(file)
    #     self.assertEqual(file.filename, self.mock_drawing_name)
    #     self.assertEqual(file_id, file._id)

    #     logging.debug("File added to DB, file ID: %s", file_id)
    #     logging.debug("File retrieved: %s", file)

    # def test_get_drawing(self):
    #     """
    #     Testează obținerea unui fișier desen din colecția MongoDB.
    #     """
    #     self.drawing_repository.add(self.mock_drawing_name, self.mock_drawing_file)

    #     file_buffer = self.drawing_repository.get(self.mock_drawing_name)

    #     self.assertIsNotNone(file_buffer)
    #     file_buffer.seek(0)
    #     self.assertEqual(file_buffer.read(), b"This is a mock drawing file.")

    #     logging.debug("Retrieved file: %s", file_buffer)

    def test_get_drawing_not_found(self):
        """
        Testează caz când desenul nu este găsit în baza de date.
        """
        result = self.drawing_repository.get("nonexistent_drawing")
        self.assertIsNone(result)
        logging.debug("No drawing found for 'nonexistent_drawing': %s", result)

    def test_check_drawing_exists(self):
        """
        Testează verificarea existenței unui fișier desen.
        """
        self.drawing_repository.add(self.mock_drawing_name, self.mock_drawing_file)

        exists = self.drawing_repository.check_exists(self.mock_drawing_name)
        self.assertTrue(exists)

        exists = self.drawing_repository.check_exists("nonexistent_drawing")
        self.assertFalse(exists)

        logging.debug("Drawing exists: %s", exists)

    # def test_update_drawing(self):
    #     """
    #     Testează actualizarea unui fișier desen.
    #     """
    #     self.drawing_repository.add(self.mock_drawing_name, self.mock_drawing_file)

    #     updated_drawing_file = BytesIO(b"This is an updated mock drawing file.")

    #     updated_file_id = self.drawing_repository.update(self.mock_drawing_name, updated_drawing_file)

    #     file = self.fs.find_one({"filename": self.mock_drawing_name})
    #     self.assertIsNotNone(file)
    #     self.assertEqual(file.filename, self.mock_drawing_name)
    #     self.assertEqual(updated_file_id, file._id)

    #     old_file = self.fs.find_one({"filename": self.mock_drawing_name})
    #     self.assertIsNone(old_file)

    #     logging.debug("Updated file ID: %s", updated_file_id)
    #     logging.debug("Original file deleted: %s", old_file)

    def test_delete_drawing(self):
        """
        Testează ștergerea unui fișier desen.
        """
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
        """
        Eliberăm resursele după fiecare test.
        """
        self.client.close()

        # Ștergem fișierul local de desen pentru a păstra testele curate
        if os.path.exists(self.mock_drawing_path):
            os.remove(self.mock_drawing_path)


if __name__ == "__main__":
    unittest.main()
