class PerformanceTracker:
    """
    PerformanceTracker enables tracking of performance metrics with observer notifications.
    Implements the Observer Pattern to allow multiple observers to receive updates on performance changes.
    """

    def __init__(self):
        """
        Initializes the PerformanceTracker with an empty list of observers.
        """
        self.observers = []

    def register_observer(self, observer):
        """
        Registers an observer to receive performance updates.

        :param observer: Observer to register for performance notifications
        """
        self.observers.append(observer)

    def unregister_observer(self, observer):
        """
        Unregisters an observer from receiving performance updates.

        :param observer: Observer to unregister from notifications
        """
        self.observers.remove(observer)

    def notify_observers(self, metric, value):
        """
        Notifies all registered observers with the latest performance metric.

        :param metric: Name of the performance metric
        :param value: Value associated with the performance metric
        """
        for observer in self.observers:
            observer.update(metric, value)

    def track(self, metric, value):
        """
        Tracks a performance metric and notifies all observers.

        :param metric: Name of the metric being tracked
        :param value: Current value of the metric
        """
        self.notify_observers(metric, value)
