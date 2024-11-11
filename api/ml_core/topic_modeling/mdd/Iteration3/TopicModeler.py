
from Preprocessor import Preprocessor
from gensim import corpora
from gensim.models import LdaModel
from pymongo import MongoClient
from api.ml_core.topic_modeling.mdd.Iteratia3.PostTopic import PostTopic


class TopicModeler:

    def __init__(self, data):
        self.data = data
        self.processed_data = Preprocessor(self.data).preprocess()

    # using LDA
    # TODO: the implementation of LDA without libraries (later)
    def extract_topics(self):
        dictionary = corpora.Dictionary(self.processed_data)
        corpus = [dictionary.doc2bow(text) for text in self.processed_data]

        lda_model = LdaModel(corpus, num_topics=2, id2word=dictionary, passes=15)

        topics = [lda_model.show_topic(topic_id, topn=3) for topic_id in range(lda_model.num_topics)]
        return [" ".join([word for word, prob in topic]) for topic in topics]

    def save_to_db(self, connection_string, db_name, table_name):
        topics = self.extract_topics()
        post_topic = PostTopic(self.data, topics)
        client = MongoClient(connection_string)
        db = client[db_name]
        collection = db[table_name]

        collection.insert_one(post_topic.to_dict())
        client.close()
        print("Data saved to db")

