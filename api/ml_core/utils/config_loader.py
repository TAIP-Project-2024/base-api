# config_loader.py
import json
from pathlib import Path


class ConfigLoader:
    """Singleton class to load and store configuration from a JSON file."""

    _instance = None

    def __new__(cls, config_path: str):
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._config_path = config_path
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        config_file = Path(self._config_path)
        with open(config_file, 'r') as file:
            self.config = json.load(file)

    def get_config(self):
        return self.config

# Usage in other files:
# config = ConfigLoader("path/to/config.json").get_config()
