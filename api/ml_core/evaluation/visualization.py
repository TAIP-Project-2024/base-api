# visualization.py

class Visualization:
    """Handles the visualization of evaluation results. Implements the Facade pattern
    to provide a simplified interface for various visualizations."""

    def plot_precision_recall(self, precision: float, recall: float):
        """
        Plots precision and recall scores on a graph.

        Args:
            precision (float): The precision score.
            recall (float): The recall score.
        """
        # Implementation for plotting precision and recall (e.g., using matplotlib)
        print(f"Plotting Precision: {precision}, Recall: {recall}")
        # Visualization logic goes here

    def plot_f1_score(self, f1: float):
        """
        Plots the F1 score on a graph.

        Args:
            f1 (float): The F1 score.
        """
        # Implementation for plotting F1 score (e.g., using matplotlib)
        print(f"Plotting F1 Score: {f1}")
        # Visualization logic goes here
