class ConfusionMatrix:
    """
    ConfusionMatrix tracks the performance of a model in terms of true positives, true negatives,
    false positives, and false negatives, which are fundamental for calculating other metrics.
    """

    def __init__(self):
        """
        Initializes a confusion matrix with default values for each category.
        """
        self.tp = 0  # True Positives
        self.tn = 0  # True Negatives
        self.fp = 0  # False Positives
        self.fn = 0  # False Negatives

    def update(self, predictions, ground_truth):
        """
        Updates the confusion matrix based on predictions and ground truth labels.

        :param predictions: List of predicted labels
        :param ground_truth: List of actual labels
        """
        # Implementation to update the confusion matrix based on comparison
        pass

    def display(self):
        """
        Displays the current state of the confusion matrix, showing counts for TP, TN, FP, and FN.
        """
        # Implementation to display the confusion matrix values in a readable format
        pass
