import sys
import subprocess
from os.path import expandvars
from pathlib import Path
from constants import *
from config_manager import ConfigManager
from erp_gui import ErpGui


def on_submit_button_press(selected_editor, target_path):
    subprocess.Popen([selected_editor, target_path])


def on_open_config_press(selected_editor, config_path):
    print(f"open {config_path} in {selected_editor}")
    subprocess.Popen([selected_editor, config_path])


def main():
    args = sys.argv[1:]
    if not args:
        return ErpGui.make_warning_popup("No path given!")

    given_path = Path.cwd().joinpath(Path(args[0])).resolve()
    if not given_path.is_dir():
        return ErpGui.make_warning_popup("Given path is not a directory!")

    target_path = expandvars(given_path)

    config_manager = ConfigManager(CONFIG_FILE)
    success, config_data = config_manager.load_config()

    if not success:
        return ErpGui.make_warning_popup(str(config_data))

    editor_paths = [editor["path"] for editor in config_data]
    window = ErpGui(editor_paths).create_window()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break

        if event in [SUBMIT_KEY, OPEN_CONFIG_KEY]:
            selected_editor_given_path = window[EDITOR_LIST_KEY].get()
            if not selected_editor_given_path:
                ErpGui.make_warning_popup("No editor is selected!")
                continue

            selected_editor = Path(expandvars(selected_editor_given_path[0]))
            if event == SUBMIT_KEY:
                on_submit_button_press(selected_editor, target_path)
            elif event == OPEN_CONFIG_KEY:
                on_open_config_press(selected_editor, config_manager.get_config_path())

            break

    window.close()


if __name__ == "__main__":
    main()
