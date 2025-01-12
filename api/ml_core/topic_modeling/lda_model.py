import os.path

import gensim
from gensim.corpora import MmCorpus
from gensim.models import LdaModel

import langid

from api.ml_core.data_preprocess.corpus_processor import CorpusProcessor
from api.ml_core.data_preprocess.topic_modeling_preprocessor import TopicModelingPreprocessor
from api.ml_core.topic_modeling.topic_model_interface import TopicModelInterface


class LDAModel(TopicModelInterface):
    """
    LDAModel constructs and trains a Latent Dirichlet Allocation model.
    Uses the Builder Pattern for customizable configuration.
    """

    def __init__(self):
        self.num_topics = 13
        self.alpha = 'auto'
        self.beta = 'auto'
        self.passes = 1
        self.random_state = 42
        self.id2word = None
        self.dictionary = None
        self.corpus = None
        self.model = None
        self.preprocessor = TopicModelingPreprocessor()
        self.model_filename = "saved_models/lda_model.model"

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

    def train_batch(self, data):
        """
        Trains the LDA model on the provided data.

        :param data: Data for topic modeling
        """

        tokens = [self.preprocessor.preprocess(d) for d in data if langid.classify(d)[0] == 'en']
        bigram_trigrams = CorpusProcessor.bigrams_trigrams(tokens)
        batch_corpus, id2word = CorpusProcessor.remove_frequent_words(bigram_trigrams)

        if self.model is None:
            print("Training LDA model...")
            self.id2word = id2word
            self.corpus = MmCorpus.serialize("saved_models/temp_corpus.mm", batch_corpus)
            self.model = LdaModel(corpus=batch_corpus,
                                  id2word=id2word,
                                  num_topics=self.num_topics,
                                  random_state=self.random_state,
                                  update_every=1,
                                  passes=self.passes,
                                  alpha=self.alpha)
        else:
            print("Update LDA model...")
            self.id2word.add_documents(bigram_trigrams)
            self.corpus.extend(batch_corpus)
            self.model.update(batch_corpus)

        return batch_corpus

    def save_model(self):
        """
        Save the LDA model and dictionary.
        """
        print("Saving LDA model...")
        if self.model:
            self.model.save(self.model_filename)
        else:
            print("No LDA model found!")
        if self.id2word:
            self.id2word.save(self.model_filename + ".id2word")
        else:
            print("No id2word found!")


    def load_model(self):
        """
        Loads the existing LDA model if it exists.

        :return: Loaded model, corpus, and id2word
        :raises FileNotFoundError: If model or dictionary is not found
        """
        if os.path.exists(self.model_filename):
            print("Loading existing model.")
            if os.path.exists(self.model_filename):
                self.model = gensim.models.LdaModel.load(self.model_filename)
            else:
                raise FileNotFoundError("No LDA model found!")
            if os.path.exists(self.model_filename + ".id2word"):
                self.id2word = gensim.corpora.Dictionary.load(self.model_filename + ".id2word")
            else:
                raise FileNotFoundError("Dictionary file not found!")
            if os.path.exists("saved_models/temp_corpus.mm"):
                self.corpus = MmCorpus("saved_models/temp_corpus.mm")
            else:
                raise FileNotFoundError("Corpus file not found!")
            print("Loaded LDA model!")
        else:
            raise FileNotFoundError("LDA model file not found!")

        return self.model, self.id2word

    def get_topics(self, model):
        """
        Retrieves the topics from the trained LDA model.

        :return: List of topics
        """

        topics = model.print_topics(num_topics=self.num_topics, num_words=30)

        sorted_topics = sorted(topics, key=lambda x: x[0])

        return sorted_topics

    def analyze(self, text):
        """
        Get the topic distribution for a single document (text).

        :param text: The input text (e.g., a Reddit title)
        :return: List of (topic_id, probability) tuples
        """
        preprocessed_text = self.preprocessor.preprocess(text)
        bow = self.id2word.doc2bow(preprocessed_text)
        return self.model.get_document_topics(bow)
