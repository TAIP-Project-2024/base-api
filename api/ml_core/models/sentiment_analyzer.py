# sentiment_analyzer.py

import torch.nn as nn
from transformers import BertModel


class SentimentAnalyzer(nn.Module):
    """Defines a BERT-based model for sentiment analysis, using the Adapter Pattern to customize BERT's output."""

    def __init__(self, num_classes: int = 2):
        """
        Initializes the SentimentAnalyzer with BERT backbone.

        Args:
            num_classes (int): Number of output classes for sentiment classification.
        """
        super(SentimentAnalyzer, self).__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.classifier = nn.Linear(self.bert.config.hidden_size, num_classes)  # Classification layer

    def forward(self, input_ids, attention_mask):
        """
        Defines the forward pass for the sentiment analyzer.

        Args:
            input_ids: Token IDs for input text.
            attention_mask: Attention mask for BERT input.

        Returns:
            Output tensor after classification.
        """
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        logits = self.classifier(outputs.pooler_output)  # Use pooled output for classification
        return logits


# Adapter Pattern Example
class SentimentAdapter:
    """Adapts outputs from the BERT model for specific sentiment analysis tasks."""

    def adapt(self, bert_output):
        """
        Processes and adapts the BERT output for sentiment classification.

        Args:
            bert_output: Output from BERT.

        Returns:
            Processed output suitable for classification.
        """
        return bert_output  # Placeholder for additional processing
