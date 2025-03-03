from os.path import expandvars
from config_manager import ConfigManager
from epr_gui import EprGUI
from pathlib import Path
import sys
import subprocess


def run():
    target_dir_editor = config.repo_editor_dict.get(target_dir)
    if not target_dir_editor:
        EprGUI(config).show()

        target_dir_editor = config.repo_editor_dict.get(target_dir)
        if not target_dir_editor:
            return

    editor_path = Path(target_dir_editor)
    if not editor_path.exists():
        # EprGUI(config).show()
        return print(f"Selected editor for this repo ({editor_path}) does not exist!")

    print(f"Found editor for {target_dir}! {target_dir_editor}")
    subprocess.Popen([editor_path, target_dir])


if __name__ == "__main__":
    args = sys.argv[:1]
    # print("args: ", args)

    # target_dir = args[0]
    target_dir = "%HOME%/Documents/GitHub/EditorPerRepoGUI"
    target_dir = expandvars(target_dir)

    config = ConfigManager(target_dir)
    config.repo_editor_dict = {}

    run()