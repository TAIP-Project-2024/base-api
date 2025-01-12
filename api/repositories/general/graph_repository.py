from io import BytesIO

from django.utils.timezone import override
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from gridfs import GridFS

from api.repositories.general.file_repository import FileRepository
from api.repositories.general.security_aop import logging_and_security

# Load environment variables from a .env file
load_dotenv('.env')
DATABASE_NAME = os.environ.get("MONGO_DB_NAME")
MONGO_URI = os.environ.get("MONGO_URI")
COLLECTION_NAME = "Graphs"
# Define database and collection names

class GraphRepository(FileRepository):
    """
    Example usage:
    with GraphRepository() as graph_repository:
        f = graph_repository.get("ExampleGraph")
        ...
    Will close the connection automatically
    """
    def __init__(self):
        # Initialize MongoDB client and set up database, collection, and GridFS
        DATABASE_NAME = os.environ.get("MONGO_DB_NAME")
        MONGO_URI = os.environ.get("MONGO_URI")
        COLLECTION_NAME = "Graphs"
        super().__init__(MONGO_URI, DATABASE_NAME, COLLECTION_NAME)
