import datetime
import json
import os.path
import shutil
from util.epr_util import EprUtil
from util.constants import CONFIG_BACKUP_LOCATION, CONFIG_FILE, MAX_CONFIG_BACKUPS
from pathlib import Path


class EprConfig:
    def __init__(self):
        self.config_path = EprUtil.get_parsed_abs_path(CONFIG_FILE, Path(__file__).parent)
        self.backup_dir_path = EprUtil.get_parsed_abs_path(CONFIG_BACKUP_LOCATION, Path(__file__).parent)
        self.editors = []


    def __remove_backups_if_past_max_count(self):
        backup_dir_files = list(filter(lambda f: "config" in f.stem, self.backup_dir_path.glob("*")))
        num_files_to_remove = len(backup_dir_files) - MAX_CONFIG_BACKUPS
        if num_files_to_remove < 1:
            return

        print(f"Removing oldest {num_files_to_remove} config backups!")

        backup_dir_files.sort(key=os.path.getmtime)
        oldest_n_files = backup_dir_files[:num_files_to_remove]
        [f.unlink() for f in oldest_n_files]
        print(f"Removed old config files! {[str(f.stem) for f in oldest_n_files]}")


    def load_config(self):
        if not self.config_path.exists():
            return EprUtil.raise_epr_error(f"Error finding config! Path given: {self.config_path}")

        with open(self.config_path, "r") as f:
            json_data = json.loads(f.read())
            f.close()
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
            self.save_config()


    def backup(self):
        config_name = self.config_path.stem
        config_ext = ".".join(self.config_path.suffixes)

        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%b-%d-%y_%H.%M.%S")
        output_path = self.backup_dir_path.joinpath(f"{config_name}_{timestamp}{config_ext}")
        shutil.copy(self.config_path, output_path)
        print(f"Backup made to {output_path}")

        self.__remove_backups_if_past_max_count()