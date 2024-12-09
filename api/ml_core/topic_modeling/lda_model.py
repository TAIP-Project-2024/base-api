from gensim import corpora
from gensim.models import LdaModel
from preprocessor import preprocessing_pipeline


class LDAModel:
    """
    LDAModel constructs and trains a Latent Dirichlet Allocation model.
    Uses the Builder Pattern for customizable configuration.
    """

    def __init__(self):
        self.num_topics = 10
        self.alpha = 'symmetric'
        self.beta = None
        self.passes = 10
        self.random_state = 42
        self.dictionary = None
        self.corpus = None
        self.model = None

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

    def preprocess_data(self, data):
        return [preprocessing_pipeline(title) for title in data]

    def train(self, data):
        """
        Trains the LDA model on the provided data.

        :param data: Data for topic modeling
        """
        preprocessed_data = self.preprocess_data(data)

        self.dictionary = corpora.Dictionary(preprocessed_data)
        self.corpus = [self.dictionary.doc2bow(text) for text in preprocessed_data]

        # Use gensim's LdaModel instead of calling LDAModel constructor
        self.model = LdaModel(self.corpus, num_topics=self.num_topics, id2word=self.dictionary, alpha=self.alpha, passes=self.passes, random_state=self.random_state)

    def get_topics(self):
        """
        Retrieves the topics from the trained LDA model.

        :return: List of topics
        """
        return self.model.print_topics(num_words=5)

    def get_document_topics(self, text):
        """
        Get the topic distribution for a single document (text).

        :param text: The input text (e.g., a Reddit title)
        :return: List of (topic_id, probability) tuples
        """
        preprocessed_text = preprocessing_pipeline(text)
        bow = self.dictionary.doc2bow(preprocessed_text)
        return self.model.get_document_topics(bow)


if __name__ == '__main__':
    reddit_posts = [
        "Experts: DOGE scheme doomed because of Musk and Ramaswamy's \"meme-level understanding\" of spending",
        "US Election results spark debate on economic policy.",
        "Breaking: New climate change regulations face opposition from various states.",
        "It's incredible!! We've a fascist as a president. What a world!"
    ]

    # Create an instance of LDAModel
    lda_model = LDAModel()

    # Train the LDA model on the reddit_posts data
    lda_model.train(reddit_posts)

    # Retrieve and print the topics
    topics = lda_model.get_topics()
    for topic in topics:
        print(topic)

    # Get the topic distribution for a single Reddit post
    single_post = reddit_posts[0]
    document_topics = lda_model.get_document_topics(single_post)
    print(f"Topic distribution for '{single_post}': {document_topics}")
