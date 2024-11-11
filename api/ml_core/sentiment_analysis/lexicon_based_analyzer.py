from sentiment_analyzer import SentimentAnalyzer

from nltk.sentiment.vader import SentimentIntensityAnalyzer


class LexiconBasedAnalyzer(SentimentAnalyzer):
    """
    LexiconBasedAnalyzer extends SentimentAnalyzer, providing lexicon-based sentiment analysis.
    Uses the Decorator Pattern to add lexicon analysis functionality to the base sentiment analyzer.
    """

    def __init__(self):
        """
        Initializes the LexiconBasedAnalyzer with an empty lexicon dictionary.
        """
        super().__init__()
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):
        """
        Analyzes the sentiment of the input text using lexicon-based methods.

        :param text: Text to analyze
        :return: Sentiment score computed based on lexicon values
        """
        sentiment_scores = self.analyzer.polarity_scores(text)
        return sentiment_scores
