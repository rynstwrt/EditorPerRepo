from os.path import expandvars
from config_manager import ConfigManager
from epr_gui import EprGUI
from pathlib import Path
import sys
import subprocess


def run():
    args = sys.argv[1:]
    if not args:
        return print("No target directory was specified!")

    target_dir_path = Path(expandvars(args[0])).resolve()
    if not target_dir_path.exists():
        return print("Target repo dir does not exist!")

    config = ConfigManager(target_dir_path)
    # config.repo_editor_dict = {}

    target_dir_editor = config.repo_editor_dict.get(target_dir_path)
    if not target_dir_editor:
        EprGUI(config).show()

        target_dir_editor = config.repo_editor_dict.get(target_dir_path)
        if not target_dir_editor:
            return

    editor_path = Path(target_dir_editor)
    if not editor_path.exists():
        # TODO: Keep reopening until a valid selection is made OR until canceled
        return print(f"Selected editor for this repo ({editor_path}) does not exist!")

    print(f"Found editor for {target_dir_path}! {target_dir_editor}")
    subprocess.Popen([editor_path, target_dir_path])


if __name__ == "__main__":
    run()