class TopicModeler:
    """
    TopicModeler serves as a Facade for various topic modeling methods.
    Provides a simplified interface for performing topic modeling.
    """

    def __init__(self):
        self.model = None  # Stores the selected topic modeling method (e.g., LDA, LSA)

    def set_model(self, model):
        """
        Sets the topic modeling method to be used.

        :param model: An instance of a topic modeling class (e.g., LDAModel, LSAModel)
        """
        self.model = model

    def train(self, data):
        """
        Trains the topic modeling method on the provided data.

        :param data: Data for topic modeling
        """
        if not self.model:
            raise ValueError("No topic modeling method set.")
        self.model.train(data)

    def get_topics(self, num_topics):
        """
        Retrieves the topics discovered by the model.

        :param num_topics: Number of topics to retrieve
        :return: List of topics
        """
        if not self.model:
            raise ValueError("No topic modeling method set.")
        return self.model.get_topics(num_topics)
