class TopicModelInterface:
    """
    TopicModelInterface class is responsible for providing an interface to analyze the topics of text using
    different models.
    """

    def analyze(self, text):
        """
        Analyzes the topics of the input text using a specific topic model.

        :param text: Text to analyze
        :return: Topics derived from the analysis
        """
        raise NotImplementedError("analyze method is not implemented")
