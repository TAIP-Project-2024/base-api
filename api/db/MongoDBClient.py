from pymongo import MongoClient
from django.conf import settings


class MongoDBClient:
    _client = None

    def get_db(self):
        if self._client is None:
            self._client = MongoClient(settings.MONGODB_SETTINGS['URI'])
        return self._client[settings.MONGODB_SETTINGS['DB_NAME']]

    def __del__(self):
        if self._client is not None:
            self._client.close()
