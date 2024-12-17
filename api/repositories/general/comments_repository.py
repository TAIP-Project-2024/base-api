
from dotenv import load_dotenv
from BaseAPI.settings import BASE_DIR

import os
from pymongo import MongoClient

# Load environment variables from a .env file
load_dotenv('.env')
DATABASE_NAME = os.environ.get("MONGO_DB_NAME")
MONGO_URI = os.environ.get("MONGO_URI")
COLLECTION_NAME = "reddit_comments"
print(DATABASE_NAME)
print(MONGO_URI)
# Define database and collection names

class CommentsRepository:

    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def __del__(self):
        # Close the MongoDB client connection
        self.client.close()

    def get_comments_for_post(self, post_id):
        comments = self.collection.find({"post_id": post_id})
        return list(comments)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__del__()
