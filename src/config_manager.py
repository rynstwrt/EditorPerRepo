import sys
import pickle
from functools import reduce
from os.path import expandvars
from glob import glob
from pathlib import Path
from data_types.editor_entry import EditorEntry
from data_types.epr_data import EprData


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
        "darwin": [],  # TODO: add auto editor search for Mac
        "linux": []  # TODO: add auto editor search for Linux
    }


    def __init__(self):
        self.storage_file_path = Path(__file__).parent.joinpath(self.__STORAGE_FILE_NAME).resolve()

        self.repo_editor_dict = {}
        self.editors = self.auto_find_installed_editors()
        self.show_found_editors = True
        self.last_used_editor_path = None

        self.__load_data()


    def __load_data(self):
        print("Loading saved data!")

        if not self.storage_file_path.exists():
            print("Data file not found!")
            return

        with open(self.storage_file_path, "rb") as save_file:
            data = pickle.load(save_file)
            print("DATA:", data)
            save_file.close()

            self.repo_editor_dict = data.repo_editor_dict
            self.editors.extend(data.editors)
            self.show_found_editors = data.show_found_editors
            self.last_used_editor_path = data.last_used_editor_path if hasattr(data, "last_used_editor_path") else self.last_used_editor_path


    def save_data(self):
        print("Saving data")
        
        non_found_editors = [editor for editor in self.editors if not editor.auto_found]
        data = EprData(repo_editor_dict=self.repo_editor_dict,
                       editors=non_found_editors,
                       show_found_editors=self.show_found_editors,
                       last_used_editor_path=self.last_used_editor_path)

        with open(self.storage_file_path, "wb") as save_file:
            pickle.dump(data, save_file, pickle.HIGHEST_PROTOCOL)
            save_file.close()


    def auto_find_installed_editors(self):
        if sys.platform not in self.__COMMON_EDITOR_LOCATIONS.keys():
            return

        search_location_paths = self.__COMMON_EDITOR_LOCATIONS[sys.platform]
        found_editor_paths = [glob(str(Path(expandvars(editor_path)).resolve()), recursive=True) for editor_path in search_location_paths]
        found_editor_paths = reduce(lambda a, b: a + b, found_editor_paths)
        found_editor_paths = list(map(lambda x: str(Path(x)), found_editor_paths))

        return list(map(lambda p: EditorEntry(p, True), found_editor_paths))