import tomllib as toml
from pathlib import Path


class ConfigManager():
    def __init__(self, config_file):
        self.config_file = config_file


    def load_config(self):
        config_path = Path(__file__).parent / Path(self.config_file)
        if not config_path.exists():
            return False, f"Error finding config! Path given: {config_path}"

        try:
            with open(config_path, "rb") as file:
                config_data = toml.load(file)
                file.close()
        except Exception as err:
            print(err)
            return False, "Error while reading config!"

        editors = config_data["editor"]
        if not editors:
            return False, "No editors were found in the config!"

        return True, editors