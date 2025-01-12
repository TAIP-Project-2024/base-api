import re
import string

import gensim

from api.ml_core.data_preprocess.text_preprocessor import TextPreprocessor

class TopicModelingPreprocessor(TextPreprocessor):
    """
    TopicModelingPreprocessor specializes in preprocessing text for topic modeling tasks.
    Extends TextPreprocessor and adds methods for removing punctuation, generating tokens, and handling bigrams/trigrams.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def emoji_elimination(data):
        """
        Removes all emoji characters from the text.

        :param data: Input text
        :return: String without emojis
        """
        emoji_pattern = re.compile(
            "["
            u"\U0001F600-\U0001F64F"  # Emoticons
            u"\U0001F300-\U0001F5FF"  # Symbols & Pictographs
            u"\U0001F680-\U0001F6FF"  # Transport & Map Symbols
            u"\U0001F1E0-\U0001F1FF"  # Flags
            u"\U00002500-\U00002BEF"  # Other symbols
            u"\U00002702-\U000027B0"  # Dingbats
            u"\U000024C2-\U0001F251"  # Enclosed characters
            "]+",
            flags=re.UNICODE,
        )
        return emoji_pattern.sub(r'', data)

    @staticmethod
    def remove_punctuation(data):
        """
        Removes punctuation from the text.

        :param data: Input text
        :return: String without punctuation
        """
        return data.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def tokenize(data):
        """
        Tokenizes the input text into lowercase words using Gensim's tokenizer.

        :param data: Input string
        :return: List of tokens
        """
        tokens = gensim.utils.simple_preprocess(data)
        return tokens

    def preprocess(self, text, **kwargs):
        """
        Executes the topic modeling preprocessing pipeline, including normalization, tokenization, and lemmatization.

        :param text: Input string
        :return: List of preprocessed tokens
        """
        text = self.remove_mentions(text)
        text = self.remove_urls(text)
        text = self.hashtag_extraction(text)
        text = self.expand_contractions(text)
        text = self.lemmatize_text(text, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
        tokens = self.gen_words(text)

        return tokens


# Example usage
if __name__ == "__main__":
    topic_preprocessor = TopicModelingPreprocessor()

    sample_text = "Here's an you're stupid examples text! Visit https://example.com for more info 👍. #exampleforhashtags"

    print("\nTopic Modeling Preprocessed Text:")
    print(topic_preprocessor.preprocess(sample_text))