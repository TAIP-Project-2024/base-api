from nltk.sentiment.vader import SentimentIntensityAnalyzer


class LexiconBasedAnalyzer:
    """
    LexiconBasedAnalyzer class is responsible for analyzing the sentiment of text using lexicon-based methods.
    """

    def __init__(self):
        """
        Initializes the LexiconBasedAnalyzer with a pre-trained VADER sentiment analyzer.
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
