import subprocess
import sys
import FreeSimpleGUI as sg
import util.epr_util
from pathlib import Path
from util.global_constants import *
from epr_config import EprConfig
from epr_gui import EprGui
import util.epr_arg_parser


def on_submit_button_press(selected_editor, target_path):
    print(selected_editor, target_path)
    if not skip_opening_editors:
        subprocess.Popen([selected_editor, target_path])
    sys.exit()


def on_open_config_press(selected_editor, config_path):
    print(f"open {config_path} in {selected_editor}")
    if not skip_opening_editors:
        subprocess.Popen([selected_editor, config_path])
    sys.exit()


def main():
    target_dir_str = args["target-dir"]
    target_dir_path = util.epr_util.get_parsed_abs_path(target_dir_str, Path.cwd())
    if not target_dir_path.is_dir():
        return EprGui.make_warning_popup("Given path is not a directory!")

    try:
        epr_config = EprConfig()
        epr_config.load_config()
    except Exception as err:
        return print(err)

    editor_associated_with_dir = epr_config.get_editor_from_dir_association(target_dir_path)
    if not ignore_editor_associations and editor_associated_with_dir:
        print("associated!:", editor_associated_with_dir)
        associated_editor_path = util.epr_util.get_parsed_abs_path(editor_associated_with_dir["editor_path"], Path(__file__).parent)
        on_submit_button_press(associated_editor_path, target_dir_path)
        return

    editors = epr_config.get_editors()
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

            selected_editor_by_name = epr_config.get_editor_from_name(selected_editor_name)
            selected_editor_path_matches = selected_editor_by_name["editor_path"]
            if not selected_editor_path_matches:
                EprGui.make_warning_popup("No editor paths are assigned to that editor!")
                continue

            if window[SAVE_SELECTION_CHECKBOX_KEY].get():
                epr_config.add_dir_to_associations(selected_editor_name, target_dir_path)

            selected_editor_path = util.epr_util.get_parsed_abs_path(selected_editor_path_matches, Path(__file__).parent)

            if event == SUBMIT_KEY:
                on_submit_button_press(selected_editor_path, target_dir_path)
            elif event == OPEN_CONFIG_KEY:
                on_open_config_press(selected_editor_path, epr_config.config_path)

            break

    window.close()
    sys.exit()


if __name__ == "__main__":
    args = util.epr_arg_parser.parse_args(sys.argv)

    if args:
        ignore_editor_associations = args["ignore-editor-associations"]
        skip_opening_editors = args["skip-open-editor"]
        main()
    else:
        EprGui.make_warning_popup("No path given!")