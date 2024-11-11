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
lexicon_analyzer = LexiconBasedAnalyzer()
analyzer.set_method(lexicon_analyzer)
print(analyzer.analyze(text)) # compound provides an overall sentiment score from -1 (most negative) to +1 (most positive).


# Deep learning analysis
deep_learning_analyzer = DeepLearningAnalyzer()
analyzer.set_method(deep_learning_analyzer)
print(analyzer.analyze(text))
