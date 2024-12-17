class DataCleaner:
    """
    DataCleaner provides an interface for cleaning strategies.
    Utilizes the Strategy Pattern to allow different cleaning approaches (e.g., StopWordsCleaner, SlangCleaner).
    """

    def __init__(self, cleaning_strategy):
        """
        Initializes the DataCleaner with a specific cleaning strategy.

        :param cleaning_strategy: Strategy for data cleaning (e.g., StopWordsCleaner, SlangCleaner)
        """
        self.cleaning_strategy = cleaning_strategy

    def clean(self, data):
        """
        Abstract method to be implemented by concrete strategies.

        :param data: The raw data to clean
        """
        pass


class StopWordsCleaner(DataCleaner):
    """
    StopWordsCleaner removes common stop words from the data.
    """

    def clean(self, data):
        """
        Removes stop words from the provided data.

        :param data: The text data from which stop words will be removed
        """
        pass


class SlangCleaner(DataCleaner):
    """
    SlangCleaner handles the replacement or removal of slang terms in the data.
    """

    def clean(self, data):
        """
        Replaces or removes slang terms from the provided data.

        :param data: The text data containing slang terms
        """
        pass
