import os

from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient

from api.models.domain.reddit_post import RedditPost

load_dotenv('.env')
DATABASE_NAME = os.environ.get("MONGO_DB_NAME")
MONGO_URI = os.environ.get("MONGO_URI")
COLLECTION_NAME = "reddit_posts"
class PostsRepository:
    def __init__(self, db = None):
        if db is  None:
            self.client = MongoClient(MONGO_URI)
            self.db = self.client[DATABASE_NAME]
            self.collection = self.db[COLLECTION_NAME]
        else:
            self.collection = db.reddit_posts

    def get_all(self):
        posts_data = self.collection.find()
        return [RedditPost.from_dict(post_data) for post_data in posts_data]

    def get_all_paginated(self, page, limit):
        posts_data = self.collection.find().skip((page - 1) * limit).limit(limit)
        return [RedditPost.from_dict(post_data) for post_data in posts_data]

    def get_by_id(self, post_id: ObjectId):
        return self.collection.find_one({"_id": post_id})

    def get_by_topic(self, topic):
        return list(self.collection.find({'subreddit': topic}))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.db.client.close()
            print("con closed")
        except Exception as e:
            print("The connection has not been set by this object, so it can't be closed by it.")


