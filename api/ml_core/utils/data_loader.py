# data_loader.py

class DataLoader:
    """Loads and preprocesses datasets. Implements the Factory Method
    pattern to create different types of data loaders based on input."""

    def create_data_loader(self, data_type: str, **kwargs):
        """
        Creates a data loader based on the specified data type.

        Args:
            data_type (str): The type of data loader to create (e.g., 'csv', 'json').
            **kwargs: Additional arguments for specific data loaders.

        Returns:
            DataLoader: An instance of a data loader for the specified type.
        """
        if data_type == 'csv':
            return CSVDataLoader(**kwargs)
        elif data_type == 'json':
            return JSONDataLoader(**kwargs)
        else:
            raise ValueError("Unsupported data type")


class CSVDataLoader:
    """Loads data from CSV files."""

    def __init__(self, file_path: str):
        """Initializes the CSV data loader with a file path."""
        self.file_path = file_path

    def load_data(self):
        """Loads data from the CSV file."""
        print(f"Loading data from CSV file: {self.file_path}")
        # Logic for loading CSV data goes here


class JSONDataLoader:
    """Loads data from JSON files."""

    def __init__(self, file_path: str):
        """Initializes the JSON data loader with a file path."""
        self.file_path = file_path

    def load_data(self):
        """Loads data from the JSON file."""
        print(f"Loading data from JSON file: {self.file_path}")
        # Logic for loading JSON data goes here
