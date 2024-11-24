from io import BytesIO, StringIO

from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
from gridfs import GridFS

load_dotenv('../../../BaseAPI/.env')
DATABASE_NAME = os.environ.get("MONGO_DB_NAME")
MONGO_URI = os.environ.get("MONGO_URI")
COLLECTION_NAME = "Drawings"

class DrawingRepository:
    """
    Example usage:
    with DrawingRepository() as drawing_repository:
        f = drawing_repository.get("ExampleDrawing")
        ...
    Will close the connection automatically
    """
    def __init__(self):
        # Initialize MongoDB client and set up database, collection, and GridFS
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]
        self.fs = GridFS(self.db, collection=COLLECTION_NAME)

    def __del__(self):
        # Close the MongoDB client connection
        self.client.close()

    def add(self, name, graph_drawing_file_buffer):
        """Add a new drawing to GridFS"""
        file_id = self.fs.put(graph_drawing_file_buffer, filename=name)
        return file_id

    def get(self, name):
        """Retrieve a drawing by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            buffer = StringIO(file.read().decode("utf-8"))
            return buffer
        else:
            return None

    def update(self, name, graph_drawing_file_buffer):
        """Update an existing drawing by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            self.fs.delete(file._id)
        file_id = self.fs.put(graph_drawing_file_buffer, filename=name)
        return file_id

    def delete(self, name):
        """Delete a drawing by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            self.fs.delete(file._id)
            return True
        return False


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__del__()