import json
from util.epr_util import EprUtil


class EprConfig:
    def __init__(self):
        self.config_path = None


    def load_config(self, config_path):
        self.config_path = config_path
        if not self.config_path.exists():
            return EprUtil.raise_epr_error(f"Error finding config! Path given: {self.config_path}")

        config_file_open = open(self.config_path, "r")
        json_data = json.loads(config_file_open.read())
        config_file_open.close()

        return json_data