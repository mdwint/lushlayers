from pathlib import Path

import pytest

from lushlayers.api import compile

examples_dir = Path(__file__).parent.parent.parent / "examples"


def with_paths(pattern: str, exclude: set[str] | None = None):
    paths = sorted(examples_dir.glob(pattern))
    if exclude:
        paths = [p for p in paths if p.name not in exclude]
    return pytest.mark.parametrize("source_path", paths, ids=[p.name for p in paths])


@with_paths("*.py", exclude={"shared.py"})
def test_compile(source_path: Path):
    json_path = source_path.with_suffix(".json")
    expected_json = json_path.read_text()

    compile(source_path)
    actual_json = json_path.read_text()

    assert actual_json == expected_json
