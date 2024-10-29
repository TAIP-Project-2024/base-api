class SentimentAnalyzer:
    """
    SentimentAnalyzer acts as a Facade for different sentiment analysis methods.
    Provides a simplified interface for analyzing sentiment.
    """

    def __init__(self):
        self.method = None  # Stores the selected analysis method (lexicon or deep learning)

    def set_method(self, method):
        """
        Sets the sentiment analysis method to be used.

        :param method: A specific analyzer instance (e.g., LexiconBasedAnalyzer, DeepLearningAnalyzer)
        """
        self.method = method

    def analyze(self, text):
        """
        Analyzes the sentiment of the provided text using the selected method.

        :param text: Text to analyze
        :return: Sentiment analysis result
        """
        if not self.method:
            raise ValueError("No analysis method set.")
        return self.method.analyze(text)
