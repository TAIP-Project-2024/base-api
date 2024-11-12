from sentiment_analyzer import SentimentAnalyzer
from lexicon_based_analyzer import LexiconBasedAnalyzer
from deep_learning_analyzer import DeepLearningAnalyzer

import nltk

# Ensure VADER lexicon data is downloaded
nltk.download('vader_lexicon')

# Example usage
analyzer = SentimentAnalyzer()
text = "The product was amazing and I absolutely loved it!"

# Lexicon-based analysis
print(analyzer.lexicon_analyzer(text)) # compound provides an overall sentiment score from -1 (most negative) to +1 (most positive).


# Deep learning analysis
print(analyzer.deep_learning_analyzer(text))
