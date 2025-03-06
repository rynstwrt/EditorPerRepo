import json
from util.epr_util import EprUtil


class EprConfig:
    def __init__(self):
        self.config_path = None
        self.editors = []


    def load_config(self, config_path):
        self.config_path = config_path
        if not config_path.exists():
            return EprUtil.raise_epr_error(f"Error finding config! Path given: {config_path}")

        config_file_open = open(config_path, "r")
        json_data = json.loads(config_file_open.read())
        config_file_open.close()

        self.editors = json_data["editors"]


    def save_config(self):
        print("Saving config!")
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump({"editors": self.editors}, f, ensure_ascii=False, indent=4)


    def get_editors(self):
        return self.editors


    def get_editor_from_name(self, editor_name):
        for editor in self.editors:
            if editor["name"] == editor_name:
                return editor


    def get_editor_from_dir_association(self, dir_path):
        dir_path = dir_path if dir_path is str else str(dir_path)
        result = list(filter(lambda e: "associated_dirs" in e and dir_path in e["associated_dirs"], self.editors))
        return result[0] if result else None


    def add_dir_to_associations(self, editor_name, dir_path):
        editor = self.get_editor_from_name(editor_name)
        if not editor:
            return

        if "associated_dirs" not in editor:
            editor["associated_dirs"] = []

        dir_path = dir_path if dir_path is str else str(dir_path)
        if dir_path not in editor["associated_dirs"]:
            editor["associated_dirs"].append(dir_path)