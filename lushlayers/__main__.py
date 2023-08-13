import argparse
from pathlib import Path

from . import __version__, api


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser()
    p.add_argument("source", type=Path, help="Path to Python source file.")
    p.add_argument("-V", "--version", action="version", version=__version__)
    return p


def main() -> None:
    args = build_arg_parser().parse_args()
    api.compile(args.source)


if __name__ == "__main__":
    main()
