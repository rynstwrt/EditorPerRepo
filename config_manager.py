from functools import reduce
from os.path import expandvars
from glob import glob
from pathlib import Path
import sys


class ConfigManager:
    __COMMON_EDITOR_LOCATIONS = {
        "win32": [
            "%LOCALAPPDATA%/Programs/Microsoft VS Code/Code.exe",
            "C:/Program Files/JetBrains/*/*/webstorm64.exe",
            "C:/Program Files/JetBrains/*/*/pycharm64.exe",
            "C:/Program Files/JetBrains/*/*/idea64.exe",
            "C:/Program Files/JetBrains/*/*/clion64.exe",
            "C:/Program Files/JetBrains/*/*/webstorm.exe",
            "C:/Program Files/JetBrains/*/*/pycharm.exe",
            "C:/Program Files/JetBrains/*/*/idea.exe",
            "C:/Program Files/JetBrains/*/*/clion.exe",
            "%LOCALAPPDATA%/Atom/atom.exe",
            "C:/Program Files/Sublime Text/sublime_text.exe",
            "%APPDATA%/Sublime Text/sublime_text.exe",
            "C:/Program Files/Notepad++/notepad++.exe"
        ],
        "darwin": [],
        "linux": []
    }


    def __init__(self):
        self.show_found_editors = True

        self.editor_paths = []


    # TODO:
    def __save_data(self):
        print("Saving:", self.editor_paths, self.show_found_editors)


    # TODO:
    def __load_saved_data(self):
        self.editor_paths += []
        self.show_found_editors = True


    def get_editor_paths(self):
        print("Getting saved editor paths...")
        return self.editor_paths


    def add_editor_path(self, editor_path):
        print(f"Saving editor path {editor_path}!")
        self.editor_paths.append(editor_path)
        self.__save_data()


    def auto_find_installed_editors(self):
        if sys.platform in self.__COMMON_EDITOR_LOCATIONS.keys():
            search_location_paths = self.__COMMON_EDITOR_LOCATIONS[sys.platform]
            found_editors = [glob(expandvars(editor_path), recursive=True) for editor_path in search_location_paths]
            found_editors = reduce(lambda a, b: a + b, found_editors)
            return list(map(lambda x: Path(x), found_editors))


    def should_show_found_editors(self):
        return self.show_found_editors


    def set_show_found_editors(self, value):
        self.show_found_editors = value