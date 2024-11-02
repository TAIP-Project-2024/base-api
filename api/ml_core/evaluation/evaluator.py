class Evaluator:
    def __init__(self, evaluation_strategy):
        """
        Initializes the Evaluator with a specific evaluation strategy.

        :param evaluation_strategy: Strategy to evaluate model performance
        """
        self.evaluation_strategy = evaluation_strategy  # Strategy Pattern

    def evaluate(self, predictions, ground_truth):
        """
        Evaluates the model's predictions against the ground truth.

        :param predictions: Model predictions
        :param ground_truth: Actual labels
        :return: Evaluation metrics
        """
        return self.evaluation_strategy.calculate(predictions, ground_truth)


class PrecisionEvaluator(Evaluator):
    def calculate(self, predictions, ground_truth):
        """
        Calculates precision based on predictions and ground truth.

        :param predictions: Model predictions
        :param ground_truth: Actual labels
        :return: Precision score
        """
        # Implementation for calculating precision
        pass


class RecallEvaluator(Evaluator):
    def calculate(self, predictions, ground_truth):
        """
        Calculates recall based on predictions and ground truth.

        :param predictions: Model predictions
        :param ground_truth: Actual labels
        :return: Recall score
        """
        # Implementation for calculating recall
        pass
