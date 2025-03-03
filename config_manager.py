import sys


class ConfigManager:
    def __init__(self):
        self.saved_editor_paths = []


    def __find_common_windows_editors(self):
        print("Finding installed editors for Windows...")
        found_windows_editors = ["11111", "MMMMM"]
        [self.saved_editor_paths.append(found) for found in found_windows_editors]
        return found_windows_editors


    def get_saved_editor_paths(self):
        print("Getting saved editor paths...")
        [self.saved_editor_paths.append(f"Path {i + 1}") for i in range(10)]
        return self.saved_editor_paths


    def save_editor_path(self, editor_path):
        print(f"Saving editor path {editor_path}!")
        self.saved_editor_paths.append(editor_path)


    def find_installed_editors(self):
        platform = sys.platform

        installed_editors = []
        # Others are linux and darwin
        if platform == "win32":
            installed_editors = self.__find_common_windows_editors()
            print("Found Windows editors:", installed_editors)

        return installed_editors