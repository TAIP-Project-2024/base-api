from api.ml_core.topic_modeling.lda_model import LDAModel
# import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')
if __name__ == "__main__":
    lda_model = LDAModel()
    lda_model.load_model()

    topic_list = [
        "Political Controversy",
        "Social Commentary",
        "Election Law and Politics",
        "Political Campaign Strategy",
        "Political Charges",
        "Israel-Palestine Conflict",
        "Political Support and Threats",
        "Legal Case",
        "Political Controversy",
        "Election Case Controversy",
        "Donald Trump",
        "Legal Case/Lawsuit",
        "Abortion Access Plan"
    ]

    text = "Trump is friend with Musk!"

    results = lda_model.analyze(text)

    print(results)