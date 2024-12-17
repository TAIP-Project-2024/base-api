from gensim import corpora
from gensim.models import Phrases, TfidfModel
from gensim.models.phrases import Phraser

class CorpusProcessor:
    """
    CorpusProcessor provides utility methods for advanced text processing, including bigram/trigram generation and low-value word removal.
    """
    @staticmethod
    def bigrams_trigrams(data, min_count=5, threshold=5):
        """
        Generates bigrams and trigrams for the input corpus using Gensim's Phrases.

        :param data: List of tokenized documents
        :param min_count: Minimum frequency for phrases to be considered
        :param threshold: Threshold for phrase scoring
        :return: List of tokenized documents with bigrams and trigrams
        """
        bigram_phrases = Phrases(data, min_count=min_count, threshold=threshold)
        trigram_phrases = Phrases(bigram_phrases[data], threshold=threshold)

        bigram = Phraser(bigram_phrases)
        trigram = Phraser(trigram_phrases)

        data_bigrams = [bigram[doc] for doc in data]
        data_trigrams = [trigram[bigram[doc]] for doc in data_bigrams]

        return data_trigrams

    @staticmethod
    def remove_frequent_words(data_trigram, low_value=0.01):
        """
        Removes low-value words from a corpus based on TF-IDF scores.

        :param data_trigram: List of tokenized documents with bigrams/trigrams
        :param low_value: Minimum TF-IDF score to retain a word
        :return: Processed corpus and dictionary
        """
        id2word = corpora.Dictionary(data_trigram)
        corpus = [id2word.doc2bow(text) for text in data_trigram]

        tfidf = TfidfModel(corpus, id2word=id2word)
        words = []
        words_missing_in_tfidf = []

        for i in range(len(corpus)):
            bow = corpus[i]
            tfidf_ids = [i for i, value in tfidf[bow]]
            bow_ids = [i for i, value in bow]
            low_value_words = [i for i, value in tfidf[bow] if value < low_value]
            drops = low_value_words + words_missing_in_tfidf

            for item in drops:
                words.append(id2word[item])
            words_missing_in_tfidf = [i for i in bow_ids if i not in tfidf_ids]
            corpus[i] = [b for b in bow if b[0] not in drops]

        return corpus, id2word
