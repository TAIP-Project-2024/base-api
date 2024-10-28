# community_detection_result.py

class CommunityDetectionResult:
    """Stores the results of community detection. Implements the Observer pattern
    to allow monitoring of community changes."""

    def __init__(self):
        """Initializes a new instance of CommunityDetectionResult."""
        self.communities = {}  # Mapping of nodes to their respective communities
        self.observers = []  # List of observers to be notified of changes

    def add_community(self, node_id: str, community_id: str):
        """
        Assigns a node to a specific community.

        Args:
            node_id (str): The identifier of the node.
            community_id (str): The identifier of the community to which the node belongs.
        """
        self.communities[node_id] = community_id  # Add or update the community for the node
        self.notify_observers()  # Notify observers about the change

    def register_observer(self, observer):
        """Registers an observer to be notified of community changes."""
        self.observers.append(observer)  # Add observer to the list

    def notify_observers(self):
        """Notifies all registered observers of community changes."""
        for observer in self.observers:
            observer.update(self.communities)  # Call update method on each observer

    def get_communities(self):
        """Returns the current mapping of nodes to their communities."""
        return self.communities
