from config_manager import ConfigManager
from epr_gui import EprGUI


if __name__ == "__main__":
    config_manager = ConfigManager()
    found_windows_editors = config_manager.find_installed_editors()
    print("Found for Windows:", found_windows_editors)

    gui_manager = EprGUI(config_manager.get_saved_editor_paths())
    gui_manager.create_window()