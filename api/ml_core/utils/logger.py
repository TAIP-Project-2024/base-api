class Logger:
    """
    Logger implements the Singleton Pattern to ensure only one instance of the logger exists.
    This central logger will handle all logging operations across the application.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            # Initialize logging settings here if needed
        return cls._instance

    def log(self, message, level="INFO"):
        """
        Logs a message at the specified level.

        :param message: The message to log
        :param level: The logging level (e.g., INFO, WARNING, ERROR)
        """
        print(f"[{level}] {message}")
