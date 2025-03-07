from pathlib import Path
from util.epr_util import EprUtil


class EprArgParser:
    def __init__(self):
        pass


    def parse_args(self, args):
        args = args[1:]
        if not args:
            return

        arg_values = {
            "target-dir": EprUtil.get_parsed_abs_path(args[0], Path.cwd()),
            "skip-open-editor": "--skip-open-editor" in args,
            "ignore-editor-associations": "--ignore-editor-associations" in args
        }

        return arg_values



