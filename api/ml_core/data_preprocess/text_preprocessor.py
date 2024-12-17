import re
from abc import ABC, abstractmethod

import contractions
import spacy
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from wordsegment import segment, load


# Initialize external libraries
# nltk.download("stopwords")
# nltk.download("wordnet")
# nltk.download("punkt")
# nltk.download("averaged_perceptron_tagger")
# nltk.download("averaged_perceptron_tagger_eng")

class ResourceManager:
    """
    ResourceManager is a singleton class that manages shared resources like stopwords, Spacy models, and WordNet mappings.
    Implements the Singleton Pattern to ensure efficient use of resources.
    """
    _instance = None

    def __new__(cls):
        """
        Initializes or retrieves the singleton instance of ResourceManager.

        :return: Singleton instance of ResourceManager
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.stop_words = set(stopwords.words("english"))
            cls._instance.spacy_model = spacy.load("en_core_web_sm", disable=["parser", "ner"])
            cls._instance.wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}
        return cls._instance


class TextPreprocessor(ABC):
    """
    TextPreprocessor provides a base class for text preprocessing tasks, offering reusable methods and a common interface for specific preprocessors.
    Implements the Template Method Pattern for preprocessing workflows.
    """
    def __init__(self):
        self.resources = ResourceManager()
        load()

    @abstractmethod
    def preprocess(self, text, **kwargs):
        """
        Preprocesses the input text according to the specific requirements of the subclass.

        :param text: Input text
        :param kwargs: Additional keyword arguments for preprocessing
        :return: Processed text
        """
        pass

    @staticmethod
    def lowercase(text):
        """
        Converts text to lowercase and removes leading/trailing whitespaces.

        :param text: Input string
        :return: Lowercased string
        """
        return text.lower().strip()

    @staticmethod
    def remove_urls(text):
        """
        Removes URLs from the input text.

        :param text: Input text
        :return: String without URLs
        """
        return re.sub(r"http\S+|www.\S+", " ", text)

    @staticmethod
    def remove_mentions(text):
        """
        Removes mentions (e.g., u/username, r/subreddit) from the text.

        :param text: Input text
        :return: String without mentions
        """
        return re.sub(r'u/\S+|r/\S+', ' ', text)

    @staticmethod
    def hashtag_extraction(data):
        """
        Extracts and splits hashtags into separate words.

        :param data: Input text
        :return: String with hashtags converted to words
        """
        hashtags = re.findall(r'#\w+', data)
        for hashtag in hashtags:
            hashtag_text = hashtag.replace('#', '')
            split_hashtag = " ".join(segment(hashtag_text))
            data = data.replace(hashtag, split_hashtag)
        return data

    @staticmethod
    def expand_contractions(text):
        """
        Expands contracted forms in the text (e.g., don't -> do not).

        :param text: Input text
        :return: String with expanded contractions
        """
        return contractions.fix(text)

    def lemmatize_text(self, data, allowed_postags=None):
        """
        Lemmatizes the input text based on allowed POS tags.

        :param data: Input string
        :param allowed_postags: List of POS tags to include (optional)
        :return: Lemmatized string
        """
        doc = self.resources.spacy_model(data)
        new_text = []
        for token in doc:
            if allowed_postags is not None and token.pos_ not in allowed_postags:
                continue
            new_text.append(token.lemma_)
        return " ".join(new_text)
