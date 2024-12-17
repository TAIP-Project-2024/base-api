import pickle

import numpy as np
import torch
import torch.nn as nn
from keras.api.preprocessing.sequence import pad_sequences

from preprocess import Preprocess
from sentiment_model_interface import SentimentModelInterface


def load_lstm_model(filepath, model_class, *args, **kwargs):
    model = model_class(*args, **kwargs)
    model.load_state_dict(torch.load(filepath, map_location=torch.device('cpu'), weights_only=True))
    print(f"\nLSTM model loaded from {filepath}")
    return model


def load_tokenizer(filepath):
    with open(filepath, "rb") as f:
        tokenizer = pickle.load(f)
    print(f"Tokenizer loaded from {filepath}")
    return tokenizer


class LSTMSentimentModel(SentimentModelInterface):
    """
    LSTMSentimentModel class is responsible for analyzing the sentiment of text using long short-term memory (LSTM) models.
    """

    def __init__(self):
        """
        Initializes the LSTMSentimentModel with a pre-trained LSTM model for sentiment analysis.
        """
        super().__init__()

        self.tokenizer = load_tokenizer("models/tokenizer.pkl")
        self.model = load_lstm_model("models/lstm_model.pth", LSTMModel, np.zeros((258666, 300)), 256)
        self.max_seq_len = 72

    def analyze(self, texts):
        """
        Analyzes the sentiment of the given texts using the pre-trained LSTM model.

        :param texts: Input texts to analyze
        :return: Sentiment score derived from deep learning analysis
        """

        # Preprocess the texts
        preprocessor = Preprocess()
        preprocessed_texts = [preprocessor.preprocess(text, False, False) for text in texts]

        # Tokenize and pad sequences
        joined_texts = [' '.join(text) for text in preprocessed_texts]
        sequences = self.tokenizer.texts_to_sequences(joined_texts)
        padded_sequences = pad_sequences(sequences, maxlen=self.max_seq_len, padding="post")

        # Convert to tensor
        inputs = torch.tensor(padded_sequences, dtype=torch.long)

        # Make predictions
        outputs = self.model(inputs)
        print(outputs)
        predictions = torch.sigmoid(outputs)
        return [np.round(prediction.item(), 4).item() for prediction in predictions]


class LSTMModel(nn.Module):
    def __init__(self, embedding_matrix, hidden_dim, output_dim=1, dropout=0.2):
        super(LSTMModel, self).__init__()
        vocab_size, embedding_dim = embedding_matrix.shape

        # Embedding Layer
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.embedding.weight = nn.Parameter(torch.tensor(embedding_matrix, dtype=torch.float32))
        self.embedding.weight.requires_grad = False  # Freeze pre-trained embeddings

        # Bi-directional LSTM
        self.lstm = nn.LSTM(
            embedding_dim,
            hidden_dim,
            num_layers=2,
            dropout=0.1,  # Dropout within LSTM layers
            batch_first=True,
            bidirectional=True  # Bi-directional LSTM
        )

        # Fully Connected Layers
        self.fc = nn.Linear(hidden_dim, output_dim)

        # Dropout and Activation
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        # Embedding layer
        embedded = self.embedding(x)

        # LSTM layer
        _, (hidden, _) = self.lstm(embedded)
        hidden = hidden[-1]  # Take the final hidden state

        out = self.fc(self.dropout(hidden))
        return out
