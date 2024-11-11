class DataSplitter:
    """
    DataSplitter is responsible for splitting data into training and testing sets.
    Implements the Singleton Pattern to ensure consistent data splits across the application.
    """

    _instance = None

    def __new__(cls):
        """
        Creates a single instance of DataSplitter, ensuring only one instance exists.

        :return: Singleton instance of DataSplitter
        """
        if cls._instance is None:
            cls._instance = super(DataSplitter, cls).__new__(cls)
        return cls._instance

    def split(self, data, train_size):
        """
        Splits the data into training and testing sets based on the specified train size.

        :param data: The complete dataset to be split
        :param train_size: Proportion of data to be used for training (e.g., 0.8 for 80%)
        """
        pass
