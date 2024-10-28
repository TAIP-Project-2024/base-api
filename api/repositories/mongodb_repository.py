from pymongo import MongoClient
from db_template import DbTemplate

"""
    Concrete implementation of DbTemplateRepository:
        MongoDB Repository
"""

class MongoDB(DbTemplate):
    def __init__(self, connection_string, db_name, collection_name):
        # TODO: connection
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create(self, data):
        # TODO
        pass

    def get(self, id):
        # TODO
        pass

    def update(self, id, new_data):
        # TODO
        pass

    def delete(self, id):
        # TODO
        pass

    def close(self):
        self.client.close()