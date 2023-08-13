import importlib.util
from pathlib import Path


def compile(source: Path) -> None:
    spec = importlib.util.spec_from_file_location(source.stem, source)
    module = importlib.util.module_from_spec(spec)  # type: ignore
    spec.loader.exec_module(module)  # type: ignore
