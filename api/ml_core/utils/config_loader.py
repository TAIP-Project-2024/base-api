import json


class ConfigLoader:
    """
    ConfigLoader implements the Singleton Pattern to ensure configuration is loaded only once.
    Configuration is read from a file and can be accessed globally across the application.
    """

    _instance = None

    def __new__(cls, config_path="config.json"):
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._load_config(config_path)
        return cls._instance

    def _load_config(self, config_path):
        """
        Loads configuration from the specified JSON file.

        :param config_path: Path to the configuration file
        """
        with open(config_path, 'r') as file:
            self.config = json.load(file)

    def get(self, key, default=None):
        """
        Retrieves a configuration value.

        :param key: The configuration key
        :param default: The default value if the key is not found
        :return: The configuration value
        """
        return self.config.get(key, default)
