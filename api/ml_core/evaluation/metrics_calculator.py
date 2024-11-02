class MetricsCalculator:
    def __init__(self, metric_adapter):
        """
        Initializes the MetricsCalculator with a specific metric adapter.

        :param metric_adapter: Adapter for metrics calculation
        """
        self.metric_adapter = metric_adapter  # Adapter Pattern

    def calculate_metrics(self, predictions, ground_truth):
        """
        Calculates various evaluation metrics.

        :param predictions: Model predictions
        :param ground_truth: Actual labels
        :return: Dictionary of calculated metrics
        """
        return self.metric_adapter.adapt(predictions, ground_truth)


class CustomMetricsAdapter:
    def adapt(self, predictions, ground_truth):
        """
        Adapts predictions and ground truth for custom metric calculations.

        :param predictions: Model predictions
        :param ground_truth: Actual labels
        :return: Dictionary of custom metrics
        """
        # Implementation to calculate custom metrics
        pass
