class DataLoader:
    """
    DataLoader is an abstract base class for loading data from different sources.
    Uses the Factory Method Pattern to load data based on the source type.
    """

    @staticmethod
    def load_data(source):
        """
        Abstract method to load data from a specified source.

        :param source: The data source (e.g., file path, database connection string)
        """
        pass


class CSVDataLoader(DataLoader):
    """
    CSVDataLoader handles loading data from CSV files.
    """

    @staticmethod
    def load_data(source):
        """
        Loads data from a CSV file.

        :param source: Path to the CSV file
        """
        pass


class DatabaseDataLoader(DataLoader):
    """
    DatabaseDataLoader handles loading data from a database.
    """

    @staticmethod
    def load_data(source):
        """
        Loads data from a database source.

        :param source: Connection string or configuration for the database
        """
        pass


class APIDataLoader(DataLoader):
    """
    APIDataLoader handles loading data from an external API.
    """

    @staticmethod
    def load_data(source):
        """
        Loads data from an API source.

        :param source: Endpoint URL or API configuration details
        """
        pass
