from os.path import expandvars
from pathlib import Path
from glob import glob

from util.constants import CONFIG_FILE


VS_CODE_PATH = "%LocalAppData%/Programs/Microsoft VS Code/Code.exe"
PYCHARM_GLOB_PATH = "C:/Program Files/JetBrains/*/*/pycharm64.exe"


def get_abs_parsed_path_from_file(file_rel_path):
    script_parent_path = Path(__file__).parent
    return script_parent_path.joinpath(file_rel_path).resolve()


def get_abs_from_glob(file_rel_path):
    gl = glob(file_rel_path, recursive=True)
    print(gl)

    has_glob_pattern = not not gl
    print("has glob:", has_glob_pattern)

    after_glob_path = gl[0] if has_glob_pattern else file_rel_path
    print("after glob:", after_glob_path)

    env_parsed = expandvars(after_glob_path)
    print("expand vars:", env_parsed)

    after_env_resolved = Path(env_parsed).resolve()
    print("after env resolve:", after_env_resolved)


def parse_path_with_glob(path):
    glob_search = glob(str(path), recursive=True)
    return glob_search[0] if glob_search else path


def get_parsed_abs_path(path, relative_to_file=True):
    root_path = Path(__file__).parent if relative_to_file else Path.cwd()
    root_parse = root_path.joinpath(path)

    glob_parse = parse_path_with_glob(root_parse)

    env_parse = expandvars(glob_parse)

    return Path(env_parse).resolve()


def main():
    target_path = "./util"
    relative_to_file = True

    print(get_parsed_abs_path(target_path, relative_to_file))


    # a = get_abs_from_glob(PYCHARM_GLOB_PATH)
    # # print(a)
    #
    # print()
    # print()
    #
    # b = get_abs_from_glob(VS_CODE_PATH)
    # print(b)


if __name__ == "__main__":
    main()
