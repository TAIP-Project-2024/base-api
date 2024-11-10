from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
from gridfs import GridFS

password = os.environ.get("MONGODB_PWD")
# connection_string = f"mongodb+srv://psca:{password}@cluster0.1nnly.mongodb.net/"
connection_string = f"mongodb+srv://psca:{password}@cluster0.1nnly.mongodb.net/?ssl=true&retryWrites=false"

DATABASE_NAME = "PoliticalSentimentDB"
COLLECTION_NAME = "Graphs"

class GraphRepository:

    def __init__(self):
        self.client = MongoClient(connection_string)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]
        self.fs = GridFS(self.db, collection = COLLECTION_NAME)
        pass

    def __del__(self):
        self.client.close()


    def update(self, name, graph_file_buffer):
        """
        @name graph name
        @graph a file object
        """
        pass

    def add(self, name, graph_file_buffer):
        pass

    def get(self, name):
        """
        returns a graph_file_buffer
        """

        file = self.fs.get_one({"filename":name})
        id = file._id
        self.fs.delete(id)
        pass

    def delete(self, name):
        """
        deletes the graph with the name
        """
        pass