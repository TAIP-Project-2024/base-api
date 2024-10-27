from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

# Load environment variables and MongoDB connection string
load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://psca:{password}@cluster0.1nnly.mongodb.net/"
DATABASE_NAME = "PoliticalSentimentDB"
COLLECTION_NAME = "AnalysisResults"

class MongoRepository:
    def __init__(self):
        # Repository Pattern: Abstracts MongoDB operations
        self.client = MongoClient(connection_string)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def create(self, data):
        """Insert new data into the MongoDB collection."""
        self.collection.insert_one(data)

    def read(self, query):
        """Read data from MongoDB collection based on a query."""
        return list(self.collection.find(query))

    def update(self, query, new_data):
        """Update existing data based on a query."""
        self.collection.update_one(query, {"$set": new_data})

    def delete(self, query):
        """Delete data based on a query."""
        self.collection.delete_one(query)

    def close(self):
        self.client.close()
