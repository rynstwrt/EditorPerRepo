from glob import glob
from os.path import expandvars
from pathlib import Path


class EprError(Exception):
    pass


class EprUtil:
    @staticmethod
    def get_parsed_abs_path(target_path, root_path):
        env_parsed = expandvars(target_path)
        joined_path = root_path.joinpath(env_parsed)

        glob_search = glob(str(joined_path), recursive=True)
        glob_result = glob_search[0] if glob_search else joined_path

        return Path(glob_result).resolve()


    @staticmethod
    def raise_epr_error(message):
        raise EprError(message)
