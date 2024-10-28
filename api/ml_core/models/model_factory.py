# model_factory.py

class ModelFactory:
    """Implements the Factory Pattern to create and return model instances based on input specifications."""

    @staticmethod
    def get_model(model_type: str):
        """
        Returns an instance of the requested model type.

        Args:
            model_type (str): Type of model ('CNN' or 'BERT').

        Returns:
            An instance of CNNModel or BERTSentimentAnalyzer based on model_type.
        """
        if model_type == "CNN":
            return CNNModel()
        elif model_type == "BERT":
            return BERTSentimentAnalyzer()
        else:
            raise ValueError("Invalid model type provided.")

# Factory Pattern Example (Minimal Implementation)
# Example call: ModelFactory.get_model("CNN")
