class CommunityVisualizer:
    """
    CommunityVisualizer uses the Observer Pattern.
    Notifies registered observers when community data is updated for visualization.
    """

    def __init__(self):
        self.observers = []  # List of registered observer views

    def register_observer(self, observer):
        """
        Registers an observer for community visualization updates.

        :param observer: Observer to be notified of updates
        """
        self.observers.append(observer)

    def notify_observers(self, communities):
        """
        Notifies all registered observers with updated community data.

        :param communities: List of communities to visualize
        """
        for observer in self.observers:
            observer.update(communities)

    def visualize(self, communities):
        """
        Generates a visualization of the communities.

        :param communities: List of communities to visualize
        """
        # Notify observers to trigger visualization updates
        self.notify_observers(communities)
