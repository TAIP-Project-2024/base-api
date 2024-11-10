from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
from gridfs import GridFS

# Load environment variables from a .env file
load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://psca:{password}@cluster0.1nnly.mongodb.net/?ssl=true&retryWrites=false"

# Define database and collection names
DATABASE_NAME = "PoliticalSentimentDB"
COLLECTION_NAME = "Graphs"

class GraphRepository:

    def __init__(self):
        # Initialize MongoDB client and set up database, collection, and GridFS
        self.client = MongoClient(connection_string)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]
        self.fs = GridFS(self.db, collection=COLLECTION_NAME)

    def __del__(self):
        # Close the MongoDB client connection
        self.client.close()

    def add(self, name, graph_file_buffer):
        """Add a new graph to GridFS"""
        file_id = self.fs.put(graph_file_buffer, filename=name)
        return file_id

    def get(self, name):
        """Retrieve a graph by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            return file.read()
        else:
            return None

    def update(self, name, graph_file_buffer):
        """Update an existing graph by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            self.fs.delete(file._id)
        file_id = self.fs.put(graph_file_buffer, filename=name)
        return file_id

    def delete(self, name):
        """Delete a graph by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            self.fs.delete(file._id)
            return True
        return False
