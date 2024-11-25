import re
import string

import contractions
import gensim.utils
import spacy
from nltk.corpus import stopwords
from wordsegment import segment, load

# INITIALIZING NLTK RESOURCES (RUN ONLY FIRST TIME, THEN NEVER AGAIN XD)
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])


def url_elimination(data):
    return re.sub(r'http\S+', '', data)


def hashtag_extraction(data):
    load()
    hashtags = re.findall(r'#\w+', data)
    for hashtag in hashtags:
        hashtag = hashtag.replace('#', '')
        split_hashtag = " ".join(segment(hashtag))
        data = data.replace(f'#{hashtag}', split_hashtag)
    return data


def emoji_elimination(data):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # Emoticoane
        u"\U0001F300-\U0001F5FF"  # Simboluri și pictograme
        u"\U0001F680-\U0001F6FF"  # Transport și simboluri diverse
        u"\U0001F1E0-\U0001F1FF"  # Steaguri
        u"\U00002500-\U00002BEF"  # Simboluri diverse (chiar și chinezești)
        u"\U00002702-\U000027B0"  # Simboluri suplimentare
        u"\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r'', data)


def lowercase(data):
    return data.lower()


def punctuation_elimination(data):
    punctuation = string.punctuation
    return data.translate(str.maketrans('', '', punctuation))


def expand_contractions(data):
    return contractions.fix(data)


def tokenize(data):
    tokens = gensim.utils.simple_preprocess(data, deacc=True)
    return tokens


def stopwords_elimination(tokens):
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens


def lemmatize(tokens):
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]


def preprocessing_pipeline(data):
    data = url_elimination(data)
    data = hashtag_extraction(data)
    data = emoji_elimination(data)
    data = lowercase(data)
    data = punctuation_elimination(data)
    data = expand_contractions(data)

    tokens = tokenize(data)
    tokens = stopwords_elimination(tokens)
    tokens = lemmatize(tokens)

    return tokens


if __name__ == '__main__':
    reddit_posts = [
        "Experts: DOGE scheme doomed because of Musk and Ramaswamy's \"meme-level understanding\" of spending",
        "US Election results spark debate on economic policy.",
        "Breaking: New climate change regulations face opposition from various states.",
        "It's incredible!! We've a fascist as a president. What a world!"
    ]

    test_preprocessed_text = [
        preprocessing_pipeline(post)
        for post in reddit_posts
    ]

    print(test_preprocessed_text)
