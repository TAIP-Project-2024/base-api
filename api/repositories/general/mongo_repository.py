from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

# Load environment variables and MongoDB connection string
load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
# connection_string = f"mongodb+srv://psca:{password}@cluster0.1nnly.mongodb.net/"
connection_string = f"mongodb+srv://psca:{password}@cluster0.1nnly.mongodb.net/?ssl=true&retryWrites=false"

DATABASE_NAME = "PoliticalSentimentDB"
COLLECTION_NAME = "AnalysisResults"

from gridfs import GridFS

client = MongoClient(connection_string)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]
fs = GridFS(db)
cwd = os.getcwd()
print("Current working directory:", cwd)
with open("../../../resources/graphs/marvel2.graphml", "rb") as file:
    file.readli
    # Store the file in GridFS
    file_id = fs.put(file, filename="marvelGraph")

client.close()


# class MongoRepository:
#     def __init__(self):
#         # Repository Pattern: Abstracts MongoDB operations
#         client = MongoClient(connection_string)
#         db = client[DATABASE_NAME]
#         collection = db[COLLECTION_NAME]
#
#     def create(self, data):
#         """Insert new data into the MongoDB collection."""
#         collection.insert_one(data)
#
#     def read(self, query):
#         """Read data from MongoDB collection based on a query."""
#         return list(collection.find(query))
#
#     def update(self, query, new_data):
#         """Update existing data based on a query."""
#         collection.update_one(query, {"$set": new_data})
#
#     def delete(self, query):
#         """Delete data based on a query."""
#         collection.delete_one(query)
#
#     def close(self):
#         client.close()
