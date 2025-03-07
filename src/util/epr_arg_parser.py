import util.epr_util
from pathlib import Path


def parse_args(args):
    args = args[1:]
    if not args:
        return

    arg_values = {
        "target-dir": util.epr_util.get_parsed_abs_path(args[0], Path.cwd()),
        "skip-open": "--skip-open" in args,
        "ignore-saved": "--ignore-saved" in args
    }

    return arg_values