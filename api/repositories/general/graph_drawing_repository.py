from abc import abstractmethod
from io import BytesIO, StringIO
from dotenv import load_dotenv, find_dotenv
import os

from pymongo import MongoClient

from gridfs import GridFS

from api.repositories.general.file_repository import FileRepository
from api.repositories.general.security_aop import logging_and_security

load_dotenv('.env')


class DrawingRepository(FileRepository):
    """
    Example usage:
    with DrawingRepository() as drawing_repository:
        f = drawing_repository.get("ExampleDrawing")
        ...
    Will close the connection automatically
    """
    def __init__(self):
        # Initialize MongoDB client and set up database, collection, and GridFS
        DATABASE_NAME = os.environ.get("MONGO_DB_NAME")
        MONGO_URI = os.environ.get("MONGO_URI")
        COLLECTION_NAME = "Drawings"
        super().__init__(MONGO_URI, DATABASE_NAME, COLLECTION_NAME)