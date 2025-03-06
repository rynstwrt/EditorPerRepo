import tomllib as toml
from pathlib import Path
from tomllib import TOMLDecodeError


class EprConfig:
    def __init__(self, config_path, util):
        self._util = util
        self._config_path = util.get_absolute_parsed_path(config_path)
    #     Path(__file__).parent / Path(config_path)


    def load_config(self):
        if not self._config_path.exists():
            return False, f"Error finding config! Path given: {self._config_path}"

        try:
            file = open(self._config_path, "rb")
            config_data = toml.load(file)
            file.close()
        except OSError as err:
            print(err)
            return False, "Error while reading config!"
        except TOMLDecodeError as err:
            print(err)
            return False, "Error while parsing config TOML! (Check your config)"

        editors = config_data["editor"]
        if not editors:
            return False, "No editors were found in the config!"

        return True, editors


    def get_config_path(self):
        return self._config_path