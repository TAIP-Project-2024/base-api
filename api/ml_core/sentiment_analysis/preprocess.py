import re

import nltk
from nltk import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
import contractions

from abbreviations import abbreviations

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('averaged_perceptron_tagger_eng')

class Preprocess:
    def __init__(self):
        self.stop_words = stopwords.words("english")
        self.stemmer = SnowballStemmer("english")
        self.lemmatizer = WordNetLemmatizer()
        self.wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}

    def preprocess(self, text, rm_stop_words=False, lemmatize=False):
        # Lowercase and strip the text
        text = text.lower().strip()

        # Remove mentions
        text = re.sub(r'@\S+', ' ', text)

        # Remove hashtags
        text = re.sub(r'#\S+', ' ', text)

        # Removing URLs
        text = re.sub(r'http\S+|www.\S+', ' ', text)

        # Convert abbreviations to words
        text = self.convert_chat_words(text)

        # Remove contractions
        text = contractions.fix(text)

        # Remove punctuation, numbers, and special characters
        text = re.sub(r'[^A-Za-z\s]', ' ', text)

        # Tokenize the text
        words = word_tokenize(text)

        # Remove stop words
        if rm_stop_words:
            words = [word for word in words if word not in self.stop_words]

        # Lemmatize the text
        if lemmatize:
            words = self.lemmatize_text(words)

        return words

    def lemmatize_text(self, words):
        # Get the POS tags for the words
        pos_tags = nltk.pos_tag(words)

        # Perform lemmatization
        lemmatized_words = []

        for word, tag in pos_tags:
            # Map the POS tag to WordNet POS tag
            pos = self.wordnet_map.get(tag[0].upper(), wordnet.NOUN)
            # Lemmatize the word with the appropriate POS tag
            lemmatized_word = self.lemmatizer.lemmatize(word, pos=pos)
            # Add the lemmatized word to the list
            lemmatized_words.append(lemmatized_word)

        return lemmatized_words

    @staticmethod
    def preprocess_bert(text):
        new_text = []
        for t in text.split(" "):
            # placeholders for reddit data (BERT is trained on Twitter data)
            t = '@user' if t.startswith('u/') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            t = 'www' if t.startswith('www') else t
            t = 'subreddit' if t.startswith('r/') and len(t) > 1 else t
            new_text.append(t)
        return " ".join(new_text)

    @staticmethod
    def convert_chat_words(text):
        words = text.split()
        converted_words = []
        for word in words:
            if word.lower() in abbreviations:
                converted_words.append(abbreviations[word.lower()])
            else:
                converted_words.append(word)
        converted_text = " ".join(converted_words)
        return converted_text
