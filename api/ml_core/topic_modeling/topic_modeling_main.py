from api.ml_core.models.model_factory import ModelFactory


if __name__ == "__main__":
    lda_model = ModelFactory.create_model("topic", "lda")
    model, corpus, id2word = lda_model.train(None)
    topic_distribution = lda_model.analyze("Trump is a republican and I like pizza")
    topic_distribution = sorted(topic_distribution, key=lambda x: x[1], reverse=True)

    topic_list = ["Political Commentary/Games", "Gaming Technology and Services", "Mobile Phone Filmmaking",
              "Software and Technology", "Cybersecurity"]

    topics = lda_model.get_topics(model)

    print(topics)
    print(topic_distribution)
    print([topic_list[topic[0]] for topic in topic_distribution])
