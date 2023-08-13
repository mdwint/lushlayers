from enum import Enum

from pydantic import BaseModel


class KeyCode(Enum):
    left_shift = "lsft"
    left_control = "lctl"
    left_command = "lcmd"
    left_option = "lopt"
    right_shift = "rsft"
    right_control = "rctl"
    right_command = "rcmd"
    right_option = "ropt"
    fn = "fn"

    backslash = "\\"
    caps_lock = "caps"
    close_bracket = "]"
    comma = ","
    delete_or_backspace = "bspc"
    equal_sign = "="
    escape = "esc"
    grave_accent_and_tilde = "`"
    hyphen = "-"
    non_us_backslash = "nubs"
    open_bracket = "["
    period = "."
    quote = "'"
    return_or_enter = "ret"
    semicolon = ";"
    slash = "/"
    spacebar = "spc"
    tab = "tab"

    up_arrow = "up"
    down_arrow = "down"
    left_arrow = "left"
    right_arrow = "rght"

    f1 = "f1"
    f2 = "f2"
    f3 = "f3"
    f4 = "f4"
    f5 = "f5"
    f6 = "f6"
    f7 = "f7"
    f8 = "f8"
    f9 = "f9"
    f10 = "f10"
    f11 = "f11"
    f12 = "f12"

    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"
    _6 = "6"
    _7 = "7"
    _8 = "8"
    _9 = "9"

    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"
    g = "g"
    h = "h"
    i = "i"
    j = "j"
    k = "k"
    l = "l"  # noqa
    m = "m"
    n = "n"
    o = "o"
    p = "p"
    q = "q"
    r = "r"
    s = "s"
    t = "t"
    u = "u"
    v = "v"
    w = "w"
    x = "x"
    y = "y"
    z = "z"

    @property
    def code(self) -> str:
        return self.name.strip("_")


class ModifiedKey(Enum):
    less_than = "<"
    greater_than = ">"
    open_curly = "{"
    close_curly = "}"
    open_paren = "("
    close_paren = ")"
    double_quote = '"'
    colon = ":"
    pipe = "|"
    question_mark = "?"
    exclamation_mark = "!"
    plus_sign = "+"
    underscore = "_"
    tidle = "~"
    at_sign = "@"
    number_sign = "#"
    dollar_sign = "$"
    percent_sign = "%"
    caret = "^"
    ampersand = "&"
    asterisk = "*"

    @property
    def combination(self) -> list[KeyCode]:
        try:
            return _modifier_combos[self]
        except KeyError:
            raise NotADirectoryError(self)


_modifier_combos: dict[ModifiedKey, list[KeyCode]] = {
    ModifiedKey.less_than: [KeyCode.left_shift, KeyCode.comma],
    ModifiedKey.greater_than: [KeyCode.left_shift, KeyCode.period],
    ModifiedKey.open_curly: [KeyCode.left_shift, KeyCode.open_bracket],
    ModifiedKey.close_curly: [KeyCode.left_shift, KeyCode.close_bracket],
    ModifiedKey.open_paren: [KeyCode.left_shift, KeyCode._9],
    ModifiedKey.close_paren: [KeyCode.left_shift, KeyCode._0],
    ModifiedKey.double_quote: [KeyCode.left_shift, KeyCode.quote],
    # TODO
}


class Alias(BaseModel):
    pass


Key = KeyCode | ModifiedKey | Alias
Pos = tuple[int, int]


class KeyLayout(BaseModel):
    keys: dict[Pos, Key]
