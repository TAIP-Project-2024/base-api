from io import StringIO, BytesIO

from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
from gridfs import GridFS

from api.repositories.general.security_aop import logging_and_security

# Load environment variables from a .env file
load_dotenv('.env')
DATABASE_NAME = os.environ.get("MONGO_DB_NAME")
MONGO_URI = os.environ.get("MONGO_URI")
COLLECTION_NAME = "Graphs"
# Define database and collection names

class CommentsRepository:
    """
        For N posts, we have M comments
        we want to add all the comments
        for all the posts.
        We also want to retrieve
        the comments for a post
        given as parameter
    """

    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]