from ..models import SentimentModel, TopicModel, CommunityDetectionModel


class ModelFactory:
    @staticmethod
    def create_model(model_type):
        """
        Creates and returns a model based on the specified type using the Abstract Factory Pattern.

        :param model_type: Type of model to create (e.g., 'sentiment', 'topic', 'community')
        :return: An instance of the specified model
        """
        if model_type == 'sentiment':
            return SentimentModel()
        elif model_type == 'topic':
            return TopicModel()
        elif model_type == 'community':
            return CommunityDetectionModel()
        else:
            raise ValueError("Unknown model type: {}".format(model_type))
