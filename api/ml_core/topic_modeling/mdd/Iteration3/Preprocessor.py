import re
import string

import nltk
from nltk.corpus import stopwords

# before running the code, you have to download the stopwords
# nltk.download('stopwords')


class Preprocessor:
    def __init__(self, data):
        self.data = data

    def delete_emojis(self, data):
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F700-\U0001F77F"  # alchemical symbols
                                   u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                                   u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                                   u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                                   u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                                   u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                                   "]+", flags=re.UNICODE)
        data = emoji_pattern.sub(r'', data)
        return data

    def remove_tags_hashtag(self, data):
        data = data.replace("#", "")
        return data

    def tokenize(self, data):
        return nltk.tokenize.word_tokenize(data)

    def remove_punctuation(self, tokens):
       return [word for word in tokens if word not in string.punctuation]

    def remove_stopwords(self, tokens):
        return [word for word in tokens if word.lower() not in stopwords.words('english')]

    def preprocess(self):
        cleaned_data = []
        for document in self.data:
            document = self.delete_emojis(document)
            document = self.remove_tags_hashtag(document)
            tokens = self.tokenize(document)
            tokens = self.remove_punctuation(tokens)
            tokens = self.remove_stopwords(tokens)
            cleaned_data.append(tokens)
        return cleaned_data