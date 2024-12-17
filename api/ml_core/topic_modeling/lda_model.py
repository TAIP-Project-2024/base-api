import os.path

import gensim
from gensim.models import LdaModel

from api.ml_core.topic_modeling.preprocessor import Preprocessor


class LDAModel:
    """
    LDAModel constructs and trains a Latent Dirichlet Allocation model.
    Uses the Builder Pattern for customizable configuration.
    """

    def __init__(self):
        self.num_topics = 5
        self.alpha = 'auto'
        self.beta = 'auto'
        self.passes = 150
        self.random_state = 42
        self.id2word = None
        self.dictionary = None
        self.corpus = None
        self.model = None
        self.preprocessor = Preprocessor()
        self.model_filename = os.path.join("api/ml_core/topic_modeling/saved_models/lda_model.model")

    def set_num_topics(self, num_topics):
        """
        Sets the number of topics for the LDA model.

        :param num_topics: Number of topics
        :return: self
        """
        self.num_topics = num_topics
        return self

    def set_alpha(self, alpha):
        """
        Sets the alpha parameter.

        :param alpha: Alpha parameter for LDA
        :return: self
        """
        self.alpha = alpha
        return self

    def set_beta(self, beta):
        """
        Sets the beta parameter.

        :param beta: Beta parameter for LDA
        :return: self
        """
        self.beta = beta
        return self

    def train(self, data):
        """
        Trains the LDA model on the provided data.

        :param data: Data for topic modeling
        """

        if os.path.exists(self.model_filename):
            print("Loading existing model.")
            self.model = gensim.models.ldamodel.LdaModel.load(self.model_filename)
            if os.path.exists(self.model_filename + ".id2word"):
                self.id2word = gensim.corpora.Dictionary.load(self.model_filename + ".id2word")
            else:
                raise FileNotFoundError("Dictionary file not found!")

        else:
            print("Training a new model.")
            tokens = [self.preprocessor.preprocessing_pipeline(d) for d in data]
            bigram_trigrams = self.preprocessor.bigrams_trigrams(tokens)
            self.corpus, self.id2word = self.preprocessor.remove_frequent_words(bigram_trigrams)
            self.model = LdaModel(corpus=self.corpus,
                                  id2word=self.id2word,
                                  num_topics=self.num_topics,
                                  random_state=self.random_state,
                                  update_every=1,
                                  passes=self.passes,
                                  alpha=self.alpha)
        self.model.save(self.model_filename)
        return self.model, self.corpus, self.id2word

    def get_topics(self, model, corpus, id2word):
        """
        Retrieves the topics from the trained LDA model.

        :return: List of topics
        """

        topics = model.print_topics(num_topics=self.num_topics, num_words=30)

        sorted_topics = sorted(topics, key=lambda x: x[0])

        return sorted_topics

    def get_document_topics(self, text):
        """
        Get the topic distribution for a single document (text).

        :param text: The input text (e.g., a Reddit title)
        :return: List of (topic_id, probability) tuples
        """
        preprocessed_text = self.preprocessor.preprocessing_pipeline(text)
        bow = self.id2word.doc2bow(preprocessed_text)
        return self.model.get_document_topics(bow)