import importlib.util
import sys
from pathlib import Path


def compile(source: Path) -> None:
    sys.path.insert(0, str(source.parent))
    try:
        spec = importlib.util.spec_from_file_location(source.stem, source)
        module = importlib.util.module_from_spec(spec)  # type: ignore
        spec.loader.exec_module(module)  # type: ignore
    finally:
        sys.path.pop(0)
