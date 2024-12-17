class CommunityVisualizer:
    """
    CommunityVisualizer uses the Observer Pattern to allow multiple views to receive community data updates.
    Notifies all registered observers when community data is updated for visualization.
    """

    def __init__(self):
        """
        Initializes the CommunityVisualizer with an empty list of observers.
        """
        self.observers = []  # List of registered observer views

    def register_observer(self, observer):
        """
        Registers an observer to receive updates about community data.

        :param observer: Observer to be notified of updates
        """
        self.observers.append(observer)

    def notify_observers(self, communities):
        """
        Notifies all registered observers, sending them the updated community data.

        :param communities: List of communities to be visualized
        """
        for observer in self.observers:
            observer.update(communities)

    def visualize(self, communities):
        """
        Generates a visualization of the communities and notifies observers to trigger updates.

        :param communities: List of communities to be visualized
        """
        # Notify observers with the updated communities data
        self.notify_observers(communities)
