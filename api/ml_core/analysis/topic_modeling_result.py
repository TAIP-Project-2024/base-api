# topic_modeling_result.py

class TopicModelingResult:
    """Stores the results of topic modeling. Implements the Builder pattern
    for constructing topic modeling results easily."""

    def __init__(self):
        """Initializes a new instance of TopicModelingResult."""
        self.topics = []  # List to store topics
        self.document_topic_distribution = {}  # Mapping of documents to their topic distribution

    def add_topic(self, topic: str):
        """
        Adds a new topic to the result.

        Args:
            topic (str): A topic identified by the topic modeling algorithm.
        """
        self.topics.append(topic)  # Add the topic to the list

    def set_document_distribution(self, document_id: str, distribution: list):
        """
        Sets the topic distribution for a specific document.

        Args:
            document_id (str): The identifier for the document.
            distribution (list): The distribution of topics for this document.
        """
        self.document_topic_distribution[document_id] = distribution  # Store distribution for the document

    def get_summary(self):
        """Returns a summary of the topics identified in the model."""
        return {
            'topics': self.topics,
            'document_topic_distribution': self.document_topic_distribution,
        }
