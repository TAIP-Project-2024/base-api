from lexicon_based_analyzer import LexiconBasedAnalyzer
from deep_learning_analyzer import DeepLearningAnalyzer


class SentimentAnalyzer:
    """
    SentimentAnalyzer acts as a Facade, providing a unified interface for various sentiment analysis methods,
    such as lexicon-based or deep learning-based analysis.
    """

    def __init__(self):
        """
        Initializes the SentimentAnalyzer with lexicon-based and deep learning-based analyzers.
        """
        self.lexicon_analyzer = LexiconBasedAnalyzer()
        self.deep_learning_analyzer = DeepLearningAnalyzer()

    def analyze_with_lexicon(self, text):
        """
        Analyzes the sentiment of the input text using lexicon-based methods.

        :param text: Text to analyze
        :return: Sentiment score computed based on lexicon values
        """
        return self.lexicon_analyzer.analyze(text)

    def analyze_with_deep_learning(self, text):
        """
        Analyzes the sentiment of the given text using deep learning-based methods.

        :param text: Text to analyze
        :return: Sentiment score derived from deep learning analysis
        """
        return self.deep_learning_analyzer.analyze(text)
