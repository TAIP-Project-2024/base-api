import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv('.env')
DATABASE_NAME = os.environ.get("MONGO_DB_NAME")
MONGO_URI = os.environ.get("MONGO_URI")
COLLECTION_NAME = "favourite_graphs"

class FavouriteGraphsRepository:

    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def __del__(self):
        # Close the MongoDB client connection
        self.client.close()

    def get_by_user_id(self, user_id):
        return self.collection.find({"user_id": user_id})

    def save(self, favourite_graph):
        self.collection.update_one({"graph_id": favourite_graph.get('graph_id'), "user_id": favourite_graph.get('user_id')}, {"$set": favourite_graph}, upsert=True)

    def delete(self, favourite_graph):
        self.collection.delete_one({"graph_id": favourite_graph.get('graph_id'), "user_id": favourite_graph.get('user_id')})