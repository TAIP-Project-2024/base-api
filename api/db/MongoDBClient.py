from pymongo import MongoClient
from django.conf import settings

"""
    Connection Pool for MongoDB
"""

class MongoDBClient:
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = MongoClient(
                'mongodb://localhost:27017/',
                maxPoolSize=20,  # Maximum number of connections
                minPoolSize=5    # Minimum number of connections
            )
        return cls._client[settings.DATABASES['mongo']['NAME']]
