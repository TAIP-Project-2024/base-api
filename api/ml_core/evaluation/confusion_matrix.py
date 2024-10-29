class ConfusionMatrix:
    def __init__(self):
        """
        Initializes a confusion matrix with default values.
        """
        self.tp = 0  # True Positives
        self.tn = 0  # True Negatives
        self.fp = 0  # False Positives
        self.fn = 0  # False Negatives

    def update(self, predictions, ground_truth):
        """
        Updates the confusion matrix based on predictions and ground truth.

        :param predictions: Model predictions
        :param ground_truth: Actual labels
        """
        # Implementation to update the confusion matrix
        pass

    def display(self):
        """
        Displays the confusion matrix.
        """
        # Implementation to display the confusion matrix
        pass
