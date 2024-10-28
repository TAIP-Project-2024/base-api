# topic_modeler.py

from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer


class TopicModeler:
    """Defines a model for topic modeling using Latent Dirichlet Allocation (LDA).
    Implements the Singleton pattern to ensure a single instance of the model."""

    _instance = None

    def __new__(cls):
        """Singleton pattern to create a single instance of TopicModeler."""
        if cls._instance is None:
            cls._instance = super(TopicModeler, cls).__new__(cls)
            cls._instance.model = LatentDirichletAllocation(n_components=5)  # Default to 5 topics
            cls._instance.vectorizer = CountVectorizer()  # Vectorizer for text data
        return cls._instance

    def fit(self, documents):
        """
        Fits the LDA model to the provided documents.

        Args:
            documents: List of text documents to model.
        """
        doc_term_matrix = self.vectorizer.fit_transform(documents)  # Transform documents to doc-term matrix
        self.model.fit(doc_term_matrix)  # Fit LDA model

    def get_topics(self):
        """Retrieves the topics identified by the LDA model."""
        return self.model.components_  # Return the topics
