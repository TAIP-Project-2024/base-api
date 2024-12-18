import spacy
from nltk.corpus import stopwords
from nltk.corpus import wordnet


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
            # Initialize external libraries
            # nltk.download("stopwords")
            # nltk.download("wordnet")
            # nltk.download("punkt")
            # nltk.download("averaged_perceptron_tagger")
            # nltk.download("averaged_perceptron_tagger_eng")

            cls._instance = super().__new__(cls)
            cls._instance.stop_words = set(stopwords.words("english"))
            cls._instance.spacy_model = spacy.load("en_core_web_sm", disable=["parser", "ner"])
            cls._instance.wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}
        return cls._instance
