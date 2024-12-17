import re

import emoji
from nltk.tokenize import word_tokenize

from api.ml_core.data_preprocess.abbreviations import abbreviations
from api.ml_core.data_preprocess.text_preprocessor import TextPreprocessor


class SentimentAnalysisPreprocessor(TextPreprocessor):
    """
    SentimentAnalysisPreprocessor specializes in preprocessing text for sentiment analysis.
    Extends TextPreprocessor and adds methods for handling emojis, abbreviations, and stopwords.
    """
    def __init__(self):
        super().__init__()

    @staticmethod
    def convert_abbreviations(text):
        """
        Converts abbreviations (e.g., "brb" -> "be right back") using a predefined dictionary.

        :param text: Input text
        :return: String with expanded abbreviations
        """
        words = text.split()
        converted_words = []
        for word in words:
            if word.lower() in abbreviations:
                converted_words.append(abbreviations[word.lower()])
            else:
                converted_words.append(word)
        return " ".join(converted_words)

    @staticmethod
    def convert_emojis(text):
        """
        Converts emojis to descriptive text (e.g., 😀 -> ":grinning_face:").

        :param text: Input text
        :return: String with emojis converted to text
        """
        return emoji.demojize(text)

    @staticmethod
    def remove_special_characters(text):
        """
        Removes non-alphanumeric characters from the text.

        :param text: Input text
        :return: String without special characters
        """
        return re.sub(r'[^A-Za-z\s]', ' ', text)

    @staticmethod
    def tokenize(text):
        """
        Tokenizes the input text into individual words.

        :param text: Input string
        :return: List of word tokens
        """
        return word_tokenize(text)

    def preprocess(self, text, remove_stopwords=False, lemmatize=False):
        """
        Executes the sentiment analysis preprocessing pipeline, including normalization,
        tokenization, and optional stopword removal or lemmatization.

        :param text: Input string
        :param remove_stopwords: Boolean to indicate whether to remove stopwords
        :param lemmatize: Boolean to indicate whether to lemmatize tokens
        :return: List of preprocessed tokens
        """
        text = self.lowercase(text)
        text = self.remove_mentions(text)
        text = self.remove_urls(text)
        text = self.hashtag_extraction(text)

        text = self.convert_abbreviations(text)
        text = self.expand_contractions(text)
        text = self.convert_emojis(text)
        text = self.remove_special_characters(text)

        text = self.lemmatize_text(text) if lemmatize else text
        tokens = self.tokenize(text)

        if remove_stopwords:
            tokens = [word for word in tokens if word not in self.resources.stop_words]

        return tokens
