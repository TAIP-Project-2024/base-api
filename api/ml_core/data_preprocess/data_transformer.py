class DataTransformer:
    def transform(self, data):
        # Template Method for data transformation
        self.preprocess(data)
        self.normalize(data)
        self.postprocess(data)

    def preprocess(self, data):
        # Default implementation, can be overridden
        pass

    def normalize(self, data):
        # Default implementation, can be overridden
        pass

    def postprocess(self, data):
        # Default implementation, can be overridden
        pass


class CustomDataTransformer(DataTransformer):
    def preprocess(self, data):
        # Custom preprocessing logic
        pass
