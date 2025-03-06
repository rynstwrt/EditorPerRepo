import subprocess
import sys
import FreeSimpleGUI as sg
from glob import glob
from os.path import expandvars
from pathlib import Path
from constants import *
from epr_config import EprConfig
from epr_gui import EprGui
from epr_util import EprUtil
# from epr_data import EprData


def on_submit_button_press(selected_editor, target_path):
    subprocess.Popen([selected_editor, target_path])


def on_open_config_press(selected_editor, config_path):
    print(f"open {config_path} in {selected_editor}")
    subprocess.Popen([selected_editor, config_path])


def main():
    sg.theme(THEME)

    args = sys.argv[1:]
    if not args:
        return EprGui.make_warning_popup("No path given!")

    # TODO: EprUtil
    util = EprUtil(Path.cwd(), Path(__file__).parent)
    print(util.get_absolute_parsed_path("./"))
    # given_path = util.get_absolute_parsed_path(Path.cwd().joinpath(Path(args[0])).resolve())

    given_path = Path.cwd().joinpath(Path(args[0])).resolve()
    if not given_path.is_dir():
        return EprGui.make_warning_popup("Given path is not a directory!")

    target_path = expandvars(given_path)

    # TODO: EprData
    # epr_data = EprData(util)
    epr_config = EprConfig(CONFIG_FILE, util)
    success, config_data = epr_config.load_config()

    if not success:
        return EprGui.make_warning_popup(str(config_data))

    editor_paths = [editor["path"] for editor in config_data]
    window = EprGui(editor_paths).create_window()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break

        if event in [SUBMIT_KEY, OPEN_CONFIG_KEY]:
            selected_editor_given_path = window[EDITOR_LIST_KEY].get()
            if not selected_editor_given_path:
                EprGui.make_warning_popup("No editor is selected!")
                continue

            glob_search = glob(selected_editor_given_path[0], recursive=True)
            selected_editor = glob_search or selected_editor_given_path
            selected_editor = expandvars(Path(selected_editor[0]))

            if event == SUBMIT_KEY:
                on_submit_button_press(selected_editor, target_path)
            elif event == OPEN_CONFIG_KEY:
                on_open_config_press(selected_editor, epr_config.get_config_path())

            break

    window.close()
    sys.exit()


if __name__ == "__main__":
    main()
