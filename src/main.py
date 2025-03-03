import sys
import subprocess
from os.path import expandvars
from config_manager import ConfigManager
from epr_gui import EprGUI
from epr_popup import EprPopup, EprPopupTypes
from pathlib import Path


def run():
    args = sys.argv[1:]
    if not args:
        print("No target directory was specified!")
        return EprPopup().show(EprPopupTypes.TARGET_DIR_NOT_SPECIFIED)

    target_dir_path = Path(expandvars(args[0])).resolve()
    print("Target dir:", target_dir_path)
    if not target_dir_path.exists():
        print("Target repo dir does not exist!")
        return EprPopup().show(EprPopupTypes.TARGET_DIR_NOT_EXIST, given_path=str(target_dir_path))

    config = ConfigManager()
    config.repo_editor_dict = {}

    target_dir_editor = config.repo_editor_dict.get(target_dir_path)
    if not target_dir_editor:
        EprGUI(config, target_dir_path).show()

        target_dir_editor = config.repo_editor_dict.get(target_dir_path)
        if not target_dir_editor:
            return

    editor_path = Path(target_dir_editor)
    if not editor_path.exists():
        # TODO: Keep reopening until a valid selection is made OR until canceled
        print(f"Selected editor for this repo ({editor_path}) does not exist!")
        return EprPopup().show(EprPopupTypes.EDITOR_NOT_EXIST, given_path=str(editor_path))

    print(f"Found editor for {target_dir_path}! {target_dir_editor}")
    subprocess.Popen([editor_path, target_dir_path])


if __name__ == "__main__":
    run()