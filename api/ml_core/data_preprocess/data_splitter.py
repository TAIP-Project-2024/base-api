class DataSplitter:
    _instance = None  # Singleton Pattern

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataSplitter, cls).__new__(cls)
        return cls._instance

    def split(self, data, train_size):
        # Implementation to split data into training and testing sets
        pass
