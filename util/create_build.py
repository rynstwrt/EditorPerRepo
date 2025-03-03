import sys
import subprocess
import PyInstaller.__main__
from pathlib import Path
from enum import Enum, auto


DEFAULT_MAIN_FILE = "src/main.py"
DEFAULT_DATA_FOLDERS = [("src/static", "static")]
DEFAULT_SKIP_OVERWRITE_CONFIRMATION = True

DEFAULT_OUTPUT_EXEC_PATH = "./dist/main/main.exe"
DEFAULT_OUTPUT_EXEC_TARGET_DIR = "C:/Users/ryans/Dropbox/OpenSCAD Projects/8x8-LED-Matrix-Lamp"


class BuildCreator:
    PYI_CMD_TYPE = Enum("InstallCmdType",
                        [("RETURN", auto()), ("PRINT", auto()),
                         ("PRINT_ONLY", auto()), ("NONE", None)])


    def __init__(self, main_file=DEFAULT_MAIN_FILE,
                 data_folders=None,
                 skip_overwite_confirmation=DEFAULT_SKIP_OVERWRITE_CONFIRMATION,
                 output_exec_path=DEFAULT_OUTPUT_EXEC_PATH,
                 output_exec_target_dir=DEFAULT_OUTPUT_EXEC_TARGET_DIR):
        self.__main_file = self.__get_absolute_path(main_file)
        self.__data_folders = data_folders or DEFAULT_DATA_FOLDERS
        self.__skip_overwrite_confirmation = skip_overwite_confirmation

        self.__output_exec_path = self.__get_absolute_path(output_exec_path)
        self.__output_exec_target_dir = self.__get_absolute_path(output_exec_target_dir)

        self.pyinstaller_command = self.__create_pyinstaller_cmd()


    @staticmethod
    def __get_absolute_path(path_str):
        if isinstance(path_str, Path):
            return str(path_str.resolve())

        return str(Path(path_str).resolve())


    def __create_pyinstaller_cmd(self):
        pyinstaller_command = [self.__main_file]
        [pyinstaller_command.extend([f"--add-data={df[0]}:{df[1]}"]) for df in self.__data_folders]
        pyinstaller_command.append("-y") if self.__skip_overwrite_confirmation else None
        return pyinstaller_command


    def __create_pyinstaller_exec(self):
        PyInstaller.__main__.run(self.pyinstaller_command)


    def __run_output_exec(self):
        subprocess_args = [self.__output_exec_path, self.__output_exec_target_dir,
                           "--force-node-api-uncaught-exceptions-policy=true"]
        print("Subprocess args:", subprocess_args)
        subprocess.Popen(subprocess_args)


    def run(self, create_exec: bool = True, run_exec: bool = True, get_pyi_cmd: bool | PYI_CMD_TYPE = PYI_CMD_TYPE.PRINT):
        if get_pyi_cmd in [self.PYI_CMD_TYPE.PRINT, self.PYI_CMD_TYPE.PRINT_ONLY]:
            print(f"PyInstaller cmd:\n{self.pyinstaller_command}\n")
            if get_pyi_cmd is self.PYI_CMD_TYPE.PRINT_ONLY:
                return

        if create_exec:
            print("Creating PyInstaller exec...")
            self.__create_pyinstaller_exec()

        if run_exec:
            print("Running exec...")
            print("FILE:", self.__output_exec_path)
            print("TARGET:", self.__output_exec_target_dir)
            print()
            self.__run_output_exec()

        if get_pyi_cmd and (get_pyi_cmd in [self.PYI_CMD_TYPE.RETURN, True] or get_pyi_cmd not in self.PYI_CMD_TYPE):
            return self.pyinstaller_command
        else:
            return


if __name__ == "__main__":
    create_exec = False
    run_exec = False

    BuildCreator().run(
        # get_pyi_cmd=BuildCreator.PYI_CMD_TYPE.PRINT_ONLY,
        create_exec="--create" in sys.argv or create_exec,
        run_exec="--run" in sys.argv or create_exec)