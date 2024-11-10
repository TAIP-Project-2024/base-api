from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
from gridfs import GridFS

password = os.environ.get("MONGODB_PWD")
# connection_string = f"mongodb+srv://psca:{password}@cluster0.1nnly.mongodb.net/"
connection_string = f"mongodb+srv://psca:{password}@cluster0.1nnly.mongodb.net/?ssl=true&retryWrites=false"

DATABASE_NAME = "PoliticalSentimentDB"
COLLECTION_NAME = "Drawings"


class DrawingRepository:

    def __init__(self):
        self.client = MongoClient(connection_string)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]
        self.fs = GridFS(self.db, collection=COLLECTION_NAME)
        pass

    def __del__(self):
        self.client.close()


    def update(self, id, graph_drawing_file_buffer):
        pass

    def add(self, name, graph_drawing_file_buffer):
        pass

    def get(self, name):
        pass

    def delete(self, name):
        pass