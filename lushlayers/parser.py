from .keys import Alias, Key, KeyCode, KeyLayout, ModifiedKey


def parse_key_layout(source: str, aliases: dict[str, Alias]) -> KeyLayout:
    def _parse_key(token: str, row: int, col: int) -> Key | None:
        if token == "_":
            return None

        if token.startswith("@"):
            try:
                return aliases[token[1:]]
            except KeyError:
                raise ParseError(row, col, f"Unknown alias '{token}'")

        try:
            return KeyCode(token)
        except ValueError:
            pass

        try:
            return ModifiedKey(token)
        except ValueError:
            pass

        raise ParseError(row, col, f"Invalid key '{token}'")

    return KeyLayout(
        keys={
            (row, col): key
            for row, line in enumerate(source.strip().splitlines(), 1)
            for col, token in enumerate(line.strip().split(), 1)
            if (key := _parse_key(token, row, col))
        }
    )


class ParseError(Exception):
    def __init__(self, row: int, col: int, msg: str):
        super().__init__(f"({row}:{col}) {msg}")
