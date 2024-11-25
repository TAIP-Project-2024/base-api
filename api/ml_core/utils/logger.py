class Logger:
    """
    Logger provides a single instance for handling all logging operations.
    Uses the Singleton Pattern to ensure centralized logging across the application.
    """

    _instance = None

    def __new__(cls):
        """
        Ensures only one instance of Logger exists, initializing logging settings as needed.
        """
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            # Initialize additional logging configurations if needed
        return cls._instance

    def log(self, message, level="INFO"):
        """
        Logs a message at a specified logging level.

        :param message: Text message to be logged
        :param level: Logging level (e.g., INFO, WARNING, ERROR)
        """
        print(f"[{level}] {message}")
