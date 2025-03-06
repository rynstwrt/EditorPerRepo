from pathlib import Path


class EprUtil:
    def __init__(self, cwd_path, file_parent_path):
        self._cwd_path = cwd_path
        self._file_parent_path = file_parent_path
        print(self._cwd_path, self._file_parent_path)
        print(Path.cwd(), Path(__file__))


    # FOR:
    #   - Given path (from cwd())
    #   - Config file (from __file__)
    #   - For selected editor (from cwd())
    #   - For data file (from __file__)
    def get_absolute_parsed_path(self, relative_path):
        print(self._cwd_path, self._file_parent_path, relative_path)
        return relative_path
