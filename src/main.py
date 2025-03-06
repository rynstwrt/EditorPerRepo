import subprocess
import sys
import FreeSimpleGUI as sg
from pathlib import Path
from util.constants import *
from epr_config import EprConfig
from epr_gui import EprGui
from util.epr_util import EprUtil


def on_submit_button_press(selected_editor, target_path):
    print(selected_editor, target_path)
    print(Path(selected_editor).exists(), Path(target_path).exists())
    subprocess.Popen([selected_editor, target_path])


def on_open_config_press(selected_editor, config_path):
    print(f"open {config_path} in {selected_editor}")
    subprocess.Popen([selected_editor, config_path])


def main():
    sg.theme(THEME)

    args = sys.argv[1:]
    if not args:
        return EprGui.make_warning_popup("No path given!")

    target_dir_str = args[0]
    target_dir_path = EprUtil.get_parsed_abs_path(target_dir_str, Path.cwd())
    if not target_dir_path.is_dir():
        return EprGui.make_warning_popup("Given path is not a directory!")

    config_path = EprUtil.get_parsed_abs_path(CONFIG_FILE, Path(__file__).parent)
    epr_config = EprConfig()
    try:
        config_data = epr_config.load_config(config_path)
    except Exception as err:
        return print(err)

    if not config_data:
        return EprGui.make_warning_popup(str(config_data))

    editors = config_data["editors"]

    window = EprGui(editors).create_window()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break

        if event in [SUBMIT_KEY, OPEN_CONFIG_KEY]:
            selected_editor_name = window[EDITOR_LIST_KEY].get()
            if not selected_editor_name:
                EprGui.make_warning_popup("No editor is selected!")
                continue

            selected_editor_name = selected_editor_name[0]

            selected_editor_path_matches = [editor["editor_path"] for editor in editors if selected_editor_name == editor["name"]]
            if not selected_editor_path_matches:
                EprGui.make_warning_popup("No editor paths are assigned to that editor!")
                continue

            selected_editor_path = EprUtil.get_parsed_abs_path(selected_editor_path_matches[0], Path(__file__).parent)

            if event == SUBMIT_KEY:
                on_submit_button_press(selected_editor_path, target_dir_path)
            elif event == OPEN_CONFIG_KEY:
                on_open_config_press(selected_editor_path, config_path)

            break

    window.close()
    sys.exit()


if __name__ == "__main__":
    main()