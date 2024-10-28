# logger.py

class Logger:
    """Handles logging within the application. Implements the Singleton pattern
    to ensure only one logger instance is used."""

    _instance = None  # Singleton instance

    def __new__(cls):
        """Creates a new instance of Logger if it doesn't exist; otherwise returns the existing instance."""
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message: str):
        """Logs a message to the console or a file."""
        print(f"LOG: {message}")  # Replace with file logging if needed
