from io import BytesIO, StringIO
from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
from gridfs import GridFS

from api.models.domain.graph_drawing import GraphDrawing
from api.repositories.general.graph_repository import GraphRepository
from api.repositories.general.security_aop import logging_and_security

load_dotenv('.env')
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
        self.fs = GridFS(self.db, collection=COLLECTION_NAME)

    def __del__(self):
        # Close the MongoDB client connection
        self.client.close()

    @logging_and_security
    def add(self, name, graph_drawing_file_buffer):
        """Add a new drawing to GridFS"""
        file_id = self.fs.put(graph_drawing_file_buffer, filename=name)
        return file_id

    @logging_and_security
    def get(self, name):
        """Retrieve a drawing by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            buffer = BytesIO(file.read())
            return buffer
        else:
            return None

    @logging_and_security
    def update(self, name, graph_drawing_file_buffer):
        """Update an existing drawing by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            self.fs.delete(file._id)
        file_id = self.fs.put(graph_drawing_file_buffer, filename=name)
        return file_id

    @logging_and_security
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

