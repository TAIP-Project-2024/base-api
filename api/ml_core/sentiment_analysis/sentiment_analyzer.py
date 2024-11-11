class SentimentAnalyzer:
    """
    SentimentAnalyzer acts as a Facade, providing a unified interface for various sentiment analysis methods,
    such as lexicon-based or deep learning-based analysis.
    """

    def __init__(self):
        """
        Initializes SentimentAnalyzer with no selected analysis method.
        """
        self.method = None  # Stores the chosen analysis method (e.g., LexiconBasedAnalyzer, DeepLearningAnalyzer)

    def set_method(self, method):
        """
        Sets the analysis method to be used for sentiment analysis.

        :param method: Instance of a specific analyzer (e.g., LexiconBasedAnalyzer, DeepLearningAnalyzer)
        """
        self.method = method

    def analyze(self, text):
        """
        Analyzes the sentiment of the given text using the chosen analysis method.

        :param text: Text to analyze
        :return: Sentiment result provided by the selected analysis method
        """
        if not self.method:
            raise ValueError("No analysis method set.")
        return self.method.analyze(text)
