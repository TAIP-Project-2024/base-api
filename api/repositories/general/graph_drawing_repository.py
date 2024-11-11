from dotenv import load_dotenv, find_dotenv
import os
from ...db.MongoDBClient import MongoDBClient
from gridfs import GridFS

# Load environment variables from a .env file
load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://psca:{password}@cluster0.1nnly.mongodb.net/?ssl=true&retryWrites=false"

# Define database and collection names
DATABASE_NAME = "PoliticalSentimentDB"
COLLECTION_NAME = "Drawings"


class DrawingRepository:

    def __init__(self):
        # Initialize MongoDB client and set up database, collection, and GridFS
        self.db = MongoDBClient().get_db()
        self.collection = self.db[COLLECTION_NAME]
        self.fs = GridFS(self.db, collection=COLLECTION_NAME)

    def add(self, name, graph_drawing_file_buffer):
        """Add a new drawing to GridFS"""
        file_id = self.fs.put(graph_drawing_file_buffer, filename=name)
        return file_id

    def get(self, name):
        """Retrieve a drawing by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            return file.read()
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
