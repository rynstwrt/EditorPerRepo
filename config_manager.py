from functools import reduce
from os.path import expandvars
from glob import glob
from pathlib import Path
from editor_entry import EditorEntry
from epr_data import EprData
import sys
import pickle


class ConfigManager:
    __STORAGE_FILE_NAME = "epr.data"

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
        self.last_used_show_found_editors = True
        self.editors = []

        self.__load_saved_data()


    # TODO: Save editors
    def __save_data(self):
        print("Saving:", self.editors, self.last_used_show_found_editors)

        data = EprData(editors=[], last_used_show_found_editors=self.last_used_show_found_editors)

        with open(self.__STORAGE_FILE_NAME, "wb") as save_file:
            pickle.dump(data, save_file, pickle.HIGHEST_PROTOCOL)
            save_file.close()


    def __load_saved_data(self):
        print("Loading saved data!")

        if not Path(self.__STORAGE_FILE_NAME).exists():
            print("Data file not found!")
            return

        with open(self.__STORAGE_FILE_NAME, "rb") as save_file:
            data = pickle.load(save_file)
            print(data)
            save_file.close()

            self.editors = data.editors
            self.last_used_show_found_editors = data.show_found_editors


    def get_editors(self):
        print("Getting saved editor paths...")
        return self.editors


    def add_editor(self, editor: EditorEntry):
        print(f"Saving editor path {editor.path}!")
        self.editors.append(editor)


    def auto_find_installed_editors(self):
        if sys.platform not in self.__COMMON_EDITOR_LOCATIONS.keys():
            return

        search_location_paths = self.__COMMON_EDITOR_LOCATIONS[sys.platform]
        found_editor_paths = [glob(expandvars(editor_path), recursive=True) for editor_path in search_location_paths]
        found_editor_paths = reduce(lambda a, b: a + b, found_editor_paths)
        found_editor_paths = list(map(lambda x: str(Path(x)), found_editor_paths))

        return list(map(lambda p: EditorEntry(p, True), found_editor_paths))


    def should_show_found_editors(self):
        return self.last_used_show_found_editors


    def set_show_found_editors(self, value):
        self.last_used_show_found_editors = value
        self.__save_data()