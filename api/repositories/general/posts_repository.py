from bson import ObjectId


class PostsRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        pass

    def get_all_paginated(self, page, limit):
        pass

    def get_by_id(self, post_id):
        pass

    def create(self, post):
        pass

    def update(self, post_id, post):
        pass

    def delete(self, post_id):
        pass
