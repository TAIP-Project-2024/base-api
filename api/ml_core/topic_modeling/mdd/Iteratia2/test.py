from Preprocessor import Preprocessor
from TopicModeler import TopicModeler

def main():
    raw_data = [
        "I love programming! #coding #Python 😊",
        "Data science is amazing. #MachineLearning 🚀",
        "Deep learning models require a lot of data."
    ]

    TopicModeler(raw_data).extract_topics()

if __name__ == '__main__':
    main()