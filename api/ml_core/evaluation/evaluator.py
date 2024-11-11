class Evaluator:
    """
    Evaluator provides an interface to evaluate model performance using a specified metric calculation strategy.
    Implements the Strategy Pattern, allowing interchangeable evaluation strategies.
    """

    def __init__(self, evaluation_strategy):
        """
        Initializes the Evaluator with a specific strategy for evaluation.

        :param evaluation_strategy: Strategy for evaluating model performance (e.g., PrecisionEvaluator, RecallEvaluator)
        """
        self.evaluation_strategy = evaluation_strategy

    def evaluate(self, predictions, ground_truth):
        """
        Evaluates the model's predictions against the ground truth using the chosen evaluation strategy.

        :param predictions: Model predictions as a list of labels
        :param ground_truth: Actual labels to compare against predictions
        :return: Evaluation metrics as calculated by the strategy
        """
        return self.evaluation_strategy.calculate(predictions, ground_truth)


class PrecisionEvaluator(Evaluator):
    """
    PrecisionEvaluator calculates the precision of a model's predictions.
    Extends Evaluator by providing a specific calculation method for precision.
    """

    def calculate(self, predictions, ground_truth):
        """
        Calculates the precision, defined as TP / (TP + FP).

        :param predictions: Model predictions as a list of labels
        :param ground_truth: Actual labels to compare against predictions
        :return: Precision score as a float
        """
        # Implementation for calculating precision
        pass


class RecallEvaluator(Evaluator):
    """
    RecallEvaluator calculates the recall of a model's predictions.
    Extends Evaluator by providing a specific calculation method for recall.
    """

    def calculate(self, predictions, ground_truth):
        """
        Calculates the recall, defined as TP / (TP + FN).

        :param predictions: Model predictions as a list of labels
        :param ground_truth: Actual labels to compare against predictions
        :return: Recall score as a float
        """
        # Implementation for calculating recall
        pass
