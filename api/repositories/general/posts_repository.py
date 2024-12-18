from bson import ObjectId

from api.models.domain.reddit_post import RedditPost


class PostsRepository:
    def __init__(self, db):
        self.collection = db.reddit_posts

    def get_all(self):
        posts_data = self.collection.find()
        return [RedditPost.from_dict(post_data) for post_data in posts_data]

    def get_all_paginated(self, page, limit):
        posts_data = self.collection.find().skip((page - 1) * limit).limit(limit)
        return [RedditPost.from_dict(post_data) for post_data in posts_data]

    def get_by_id(self, post_id: ObjectId):
        return self.collection.find_one({"_id": post_id})
