import numpy as np
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig

from api.ml_core.data_preprocess.bert_preprocessor import BertPreprocessor
from api.ml_core.sentiment_analysis.sentiment_model_interface import SentimentModelInterface


class BertSentimentModel(SentimentModelInterface):
    """
    BertSentimentModel class is responsible for analyzing the sentiment of text using BERT models.
    """

    def __init__(self):
        """
        Initializes the BertSentimentModel with a pre-trained BERT model for sentiment analysis.
        """
        super().__init__()

        model_path = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.config = AutoConfig.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)

    def analyze(self, text):
        """
        Analyzes the sentiment of the given text using the deep learning model.

        :param text: Input text to analyze
        :return: Sentiment score derived from deep learning analysis
        """
        preprocessor = BertPreprocessor()
        text = preprocessor.preprocess(text)

        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        # Compute continuous sentiment score
        sentiment_score = np.dot(scores, [0, 1, 2])

        ranking = np.argsort(scores)
        ranking = ranking[::-1]

        predicted_label = ranking[0]
        predicted_score = np.round(float(scores[predicted_label]), 4)
        print(f"Predicted: {self.config.id2label[predicted_label]}, "
              f"Class Percentage: {predicted_score}\n",
              f"Continuous Score: {sentiment_score:.2f} (0=negative, 1=neutral, 2=positive)")

        # Return the continuous sentiment score with 4 decimal places
        return np.round(sentiment_score, 4).item(), self.config.id2label[predicted_label]
