from ..models import SentimentModel, TopicModel, CommunityDetectionModel


class ModelFactory:
    """
    ModelFactory is an Abstract Factory that creates instances of different model types
    (e.g., SentimentModel, TopicModel, CommunityDetectionModel) based on the specified model type.
    Implements the Abstract Factory Pattern to encapsulate model instantiation.
    """

    @staticmethod
    def create_model(model_type):
        """
        Creates and returns a model instance based on the specified type.

        :param model_type: Type of model to create (e.g., 'sentiment', 'topic', 'community')
        :return: An instance of the specified model type
        :raises ValueError: If an unknown model type is specified
        """
        if model_type == 'sentiment':
            return SentimentModel()
        elif model_type == 'topic':
            return TopicModel()
        elif model_type == 'community':
            return CommunityDetectionModel()
        else:
            raise ValueError("Unknown model type: {}".format(model_type))
