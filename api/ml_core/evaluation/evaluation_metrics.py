# evaluation_metrics.py

class EvaluationMetrics:
    """Calculates various evaluation metrics for model performance.
    Implements the Singleton pattern to ensure only one instance is used."""

    _instance = None  # Singleton instance

    def __new__(cls):
        """Creates a new instance of EvaluationMetrics if it doesn't exist; otherwise returns the existing instance."""
        if cls._instance is None:
            cls._instance = super(EvaluationMetrics, cls).__new__(cls)
        return cls._instance

    def precision(self, true_positives: int, false_positives: int) -> float:
        """
        Calculates precision based on true positives and false positives.

        Args:
            true_positives (int): Number of true positive predictions.
            false_positives (int): Number of false positive predictions.

        Returns:
            float: The precision score.
        """
        if true_positives + false_positives == 0:
            return 0.0
        return true_positives / (true_positives + false_positives)

    def recall(self, true_positives: int, false_negatives: int) -> float:
        """
        Calculates recall based on true positives and false negatives.

        Args:
            true_positives (int): Number of true positive predictions.
            false_negatives (int): Number of false negative predictions.

        Returns:
            float: The recall score.
        """
        if true_positives + false_negatives == 0:
            return 0.0
        return true_positives / (true_positives + false_negatives)

    def f1_score(self, precision: float, recall: float) -> float:
        """
        Calculates the F1 score based on precision and recall.

        Args:
            precision (float): The precision score.
            recall (float): The recall score.

        Returns:
            float: The F1 score.
        """
        if precision + recall == 0:
            return 0.0
        return 2 * (precision * recall) / (precision + recall)
