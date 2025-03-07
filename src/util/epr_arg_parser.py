import util.epr_util
from pathlib import Path


def parse_args(args):
    args = args[1:]

    target_dir = None if not args else util.epr_util.get_parsed_abs_path(args[0], Path.cwd())

    return {
        "target-dir": target_dir,
        "skip-open": "--skip-open" in args,
        "ignore-saved": "--ignore-saved" in args
    }