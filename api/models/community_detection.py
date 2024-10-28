from datetime import datetime

class CommunityDetection:
    def __init__(self):
        self.communities_detected = []
        self.timestamp = None

    def detect_communities(self, data):
        """Simulate community detection and set the result."""
        self.communities_detected = [
            {"id": 1, "members": 10},
            {"id": 2, "members": 15}
        ]
        self.timestamp = datetime.now()
        return self.to_dict()

    def get_communities_detected(self):
        return self.communities_detected

    def get_timestamp(self):
        return self.timestamp

    def set_communities_detected(self, communities):
        self.communities_detected = communities

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def to_dict(self):
        """Return the object's attributes as a dictionary."""
        return {
            "communities_detected": self.communities_detected,
            "timestamp": self.timestamp
        }
