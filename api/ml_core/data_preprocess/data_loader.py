class DataLoader:
    @staticmethod
    def load_data(source):
        # Factory Method to load data based on the source type
        pass


class CSVDataLoader(DataLoader):
    @staticmethod
    def load_data(source):
        # Implementation for loading CSV data
        pass


class DatabaseDataLoader(DataLoader):
    @staticmethod
    def load_data(source):
        # Implementation for loading data from a database
        pass


class APIDataLoader(DataLoader):
    @staticmethod
    def load_data(source):
        # Implementation for loading data from an API
        pass
