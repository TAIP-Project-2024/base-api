class DataTransformer:
    """
    DataTransformer provides a base structure for data transformation steps.
    Implements the Template Method Pattern to ensure consistent steps (preprocess, normalize, postprocess),
    while allowing custom transformation logic in derived classes.
    """

    def transform(self, data):
        """
        Transforms data by applying preprocessing, normalization, and postprocessing.

        :param data: The data to transform
        """
        self.preprocess(data)
        self.normalize(data)
        self.postprocess(data)

    def preprocess(self, data):
        """
        Default preprocessing step; can be overridden by subclasses.

        :param data: The data to preprocess
        """
        pass

    def normalize(self, data):
        """
        Default normalization step; can be overridden by subclasses.

        :param data: The data to normalize
        """
        pass

    def postprocess(self, data):
        """
        Default postprocessing step; can be overridden by subclasses.

        :param data: The data to postprocess
        """
        pass


class CustomDataTransformer(DataTransformer):
    """
    CustomDataTransformer allows for specific customization in data transformation.
    Overrides the preprocess method to provide custom preprocessing logic.
    """

    def preprocess(self, data):
        """
        Custom preprocessing logic for transforming the data.

        :param data: The data to preprocess
        """
        pass
