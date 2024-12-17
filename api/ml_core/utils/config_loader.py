import json


class ConfigLoader:
    """
    ConfigLoader uses the Singleton Pattern to ensure that configuration data is loaded only once,
    making it accessible globally within the application.
    """

    _instance = None

    def __new__(cls, config_path="config.json"):
        """
        Ensures a single instance of ConfigLoader is created and loads configuration from a specified file.

        :param config_path: Path to the JSON configuration file
        :return: Singleton instance of ConfigLoader
        """
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._load_config(config_path)
        return cls._instance

    def _load_config(self, config_path):
        """
        Loads configuration from the JSON file at the specified path.

        :param config_path: Path to the configuration file
        """
        with open(config_path, 'r') as file:
            self.config = json.load(file)

    def get(self, key, default=None):
        """
        Retrieves a configuration value based on a key.

        :param key: Configuration key to look up
        :param default: Default value if key is not found
        :return: Configuration value or default if key is missing
        """
        return self.config.get(key, default)
