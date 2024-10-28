# data_preprocessor.py

from typing import List, Dict
import re
import string
import nltk
from nltk.corpus import stopwords


class DataPreprocessor:
    """Processes raw Twitter data for NLP and deep learning models."""

    def __init__(self):
        """Initialize resources for data preprocessing."""
        nltk.download("stopwords")
        self.stop_words = set(stopwords.words("english"))

    def clean_text(self, data: List[Dict]) -> List[Dict]:
        """Performs basic text cleaning on tweets.

        Args:
            data (List[Dict]): List of tweet dictionaries with raw text.

        Returns:
            List[Dict]: List of tweets with cleaned text.
        """
        for item in data:
            text = item["text"]
            text = self._remove_urls(text)
            text = self._remove_punctuation(text)
            text = self._remove_stopwords(text)
            item["cleaned_text"] = text
        return data

    def _remove_urls(self, text: str) -> str:
        """Removes URLs from the text.

        Args:
            text (str): Original tweet text.

        Returns:
            str: Text without URLs.
        """
        return re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)

    def _remove_punctuation(self, text: str) -> str:
        """Removes punctuation from the text.

        Args:
            text (str): Original tweet text.

        Returns:
            str: Text without punctuation.
        """
        return text.translate(str.maketrans("", "", string.punctuation))

    def _remove_stopwords(self, text: str) -> str:
        """Removes common stopwords from the text.

        Args:
            text (str): Text after punctuation removal.

        Returns:
            str: Text without stopwords.
        """
        words = text.split()
        return " ".join([word for word in words if word.lower() not in self.stop_words])

    def tokenize_text(self, data: List[Dict]) -> List[Dict]:
        """Tokenizes cleaned text for model readiness.

        Args:
            data (List[Dict]): List of tweet dictionaries with cleaned text.

        Returns:
            List[Dict]: List of tweets with tokenized text.
        """
        for item in data:
            item["tokens"] = item["cleaned_text"].split()
        return data

    def prepare_for_model(self, data: List[Dict]) -> List[Dict]:
        """Converts tokenized text into model-compatible format (e.g., sequence of IDs).

        Args:
            data (List[Dict]): List of tweet dictionaries with tokenized text.

        Returns:
            List[Dict]: Prepared data for model input.
        """
        # Placeholder for model preparation logic (e.g., token to ID conversion)
        for item in data:
            item["model_input"] = item["tokens"]  # Simplified for example
        return data
