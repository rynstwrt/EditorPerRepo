import subprocess
import PyInstaller.__main__
from pathlib import Path

#
# MAIN_FILE = "src/main.py"
# ADD_DATA_FOLDERS = [("src/static", "static")]
# SKIP_OVERWRITE_CONFIRMATION = True
#
# OUTPUT_EXEC_PATH = Path("./dist/main/main.exe").resolve()
# OUTPUT_EXEC_TARGET_DIR = Path("C:/Users/ryans/Dropbox/OpenSCAD Projects/8x8-LED-Matrix-Lamp").resolve()


# def __create_pyinstaller_exec():
#     pyinstaller_command = [MAIN_FILE]
#     [pyinstaller_command.extend(["--add-data", f"{df[0]}:{df[1]}"]) for df in ADD_DATA_FOLDERS]
#     pyinstaller_command.append("-y") if SKIP_OVERWRITE_CONFIRMATION else None
#
#     print("PyInstaller cmd:", pyinstaller_command)
#     PyInstaller.__main__.run(pyinstaller_command)
#
#
# def __run_exec():
#     subprocess_args = [OUTPUT_EXEC_PATH, OUTPUT_EXEC_TARGET_DIR]
#     # subprocess_args = [OUTPUT_EXEC_PATH]
#     print("Subprocess args:", subprocess_args)
#     subprocess.Popen(subprocess_args)


# if __name__ == "__main__":
    # create_pyinstaller_exec()
    # __run_exec()


class BuildCreator:
    __MAIN_FILE = "src/main.py"
    __ADD_DATA_FOLDERS = [("src/static", "static")]
    __SKIP_OVERWRITE_CONFIRMATION = True

    __OUTPUT_EXEC_PATH = Path("./dist/main/main.exe").resolve()
    __OUTPUT_EXEC_TARGET_DIR = Path("C:/Users/ryans/Dropbox/OpenSCAD Projects/8x8-LED-Matrix-Lamp").resolve()


    def __init__(self):
        self.pyinstaller_command = self.__create_pyinstaller_cmd()

    
    # ([A-Z_]{4,})
    # (__[A-Z_]{4,})
    # def __create_pyinstaller_exec(self):
    def __create_pyinstaller_cmd(self):
        pyinstaller_command = [self.__MAIN_FILE]
        [pyinstaller_command.extend(["--add-data", f"{df[0]}:{df[1]}"]) for df in self.__ADD_DATA_FOLDERS]
        pyinstaller_command.append("-y") if self.__SKIP_OVERWRITE_CONFIRMATION else None
        return pyinstaller_command


    def create_pyinstaller_exec(self):
        print("PyInstaller cmd:", self.pyinstaller_command)
        PyInstaller.__main__.run(self.pyinstaller_command)


    def run_output_exec(self):
        subprocess_args = [self.__OUTPUT_EXEC_PATH, self.__OUTPUT_EXEC_TARGET_DIR]
        # subprocess_args = [self.__OUTPUT_EXEC_PATH]
        print("Subprocess args:", subprocess_args)
        subprocess.Popen(subprocess_args)


if __name__ == "__main__":
    creator = BuildCreator()
    print(creator.pyinstaller_command)
    # creator.create_pyinstaller_exec()
    # creator.run_output_exec()