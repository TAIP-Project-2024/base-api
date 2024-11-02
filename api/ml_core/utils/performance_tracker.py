class PerformanceTracker:
    """
    PerformanceTracker uses the Observer Pattern to allow multiple observers to track performance metrics.
    Observers can register to receive updates whenever a performance metric is tracked.
    """

    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        """
        Registers an observer for performance metric updates.

        :param observer: The observer to register
        """
        self.observers.append(observer)

    def unregister_observer(self, observer):
        """
        Unregisters an observer.

        :param observer: The observer to unregister
        """
        self.observers.remove(observer)

    def notify_observers(self, metric, value):
        """
        Notifies all observers with the latest performance metric.

        :param metric: The name of the metric
        :param value: The value of the metric
        """
        for observer in self.observers:
            observer.update(metric, value)

    def track(self, metric, value):
        """
        Tracks a performance metric and notifies observers.

        :param metric: The name of the metric
        :param value: The value of the metric
        """
        # Notify all observers with the new performance metric data
        self.notify_observers(metric, value)
