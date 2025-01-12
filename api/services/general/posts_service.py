from bson import ObjectId
from BaseAPI.settings import BASE_DIR

from api.repositories.general.posts_repository import PostsRepository

class PostsService:

    def get_topic_posts(self, topic):
        with PostsRepository() as pr:
            return pr.get_by_topic(topic)

