from enum import Enum

from pydantic import BaseModel


class KeyCode(Enum):
    # Modifier keys
    caps_lock = "caps"
    left_shift = "lsft"
    left_control = "lctl"
    left_command = "lcmd"
    left_option = "lopt"
    right_shift = "rsft"
    right_control = "rctl"
    right_command = "rcmd"
    right_option = "ropt"
    fn = "fn"

    # Controls and symbols
    return_or_enter = "ret"
    escape = "esc"
    delete_or_backspace = "bspc"
    delete_forward = "del"
    tab = "tab"
    spacebar = "spc"
    hyphen = "-"
    equal_sign = "="
    open_bracket = "["
    close_bracket = "]"
    backslash = "\\"
    non_us_pound = "nup"
    semicolon = ";"
    quote = "'"
    grave_accent_and_tilde = "`"
    comma = ","
    period = "."
    slash = "/"
    non_us_backslash = "nubs"

    # Arrow keys
    up_arrow = "up"
    down_arrow = "down"
    left_arrow = "left"
    right_arrow = "rght"
    page_up = "pgup"
    page_down = "pgdn"
    home = "home"
    end = "end"

    # Function keys
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
    f13 = "f13"
    f14 = "f14"
    f15 = "f15"
    f16 = "f16"
    f17 = "f17"
    f18 = "f18"
    f19 = "f19"
    f20 = "f20"
    f21 = "f21"
    f22 = "f22"
    f23 = "f23"
    f24 = "f24"

    # Numbers
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

    # Letters
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

    # Media controls
    display_brightness_decrement = "brdn"
    display_brightness_increment = "brup"
    mission_control = "mctl"
    launchpad = "lp"
    dashboard = "dash"
    illumination_decrement = "bldn"
    illumination_increment = "blup"
    rewind = "rwnd"
    play_or_pause = "pp"
    fastforward = "ff"
    mute = "mute"
    volume_decrement = "vold"
    volume_increment = "volu"
    eject = "ejct"

    # Keypad keys
    keypad_num_lock = "nlck"
    keypad_slash = "kp/"
    keypad_asterisk = "kp*"
    keypad_hyphen = "kp-"
    keypad_plus = "kp+"
    keypad_enter = "kprt"
    keypad_1 = "kp1"
    keypad_2 = "kp2"
    keypad_3 = "kp3"
    keypad_4 = "kp4"
    keypad_5 = "kp5"
    keypad_6 = "kp6"
    keypad_7 = "kp7"
    keypad_8 = "kp8"
    keypad_9 = "kp9"
    keypad_0 = "kp0"
    keypad_period = "kp."
    keypad_equal_sign = "kp="
    keypad_comma = "kp,"

    # Virtual keys
    vk_none = "XX"

    # Keys in PC keyboards
    print_screen = "prnt"
    scroll_lock = "slck"
    pause = "paus"
    insert = "ins"

    @property
    def code(self) -> str:
        return self.name.strip("_")


class ModifiedKey(Enum):
    exclamation_mark = "!"
    at_sign = "@"
    number_sign = "#"
    dollar_sign = "$"
    percent_sign = "%"
    caret = "^"
    ampersand = "&"
    asterisk = "*"
    open_paren = "("
    close_paren = ")"
    underscore = "\\_"
    plus_sign = "+"
    open_curly = "{"
    close_curly = "}"
    colon = ":"
    double_quote = '"'
    pipe = "|"
    tidle = "~"
    less_than = "<"
    greater_than = ">"
    question_mark = "?"

    @property
    def combination(self) -> list[KeyCode]:
        try:
            return _modifier_combos[self]
        except KeyError:
            raise NotImplementedError(self)


_modifier_combos: dict[ModifiedKey, list[KeyCode]] = {
    ModifiedKey.exclamation_mark: [KeyCode.left_shift, KeyCode._1],
    ModifiedKey.at_sign: [KeyCode.left_shift, KeyCode._2],
    ModifiedKey.number_sign: [KeyCode.left_shift, KeyCode._3],
    ModifiedKey.dollar_sign: [KeyCode.left_shift, KeyCode._4],
    ModifiedKey.percent_sign: [KeyCode.left_shift, KeyCode._5],
    ModifiedKey.caret: [KeyCode.left_shift, KeyCode._6],
    ModifiedKey.ampersand: [KeyCode.left_shift, KeyCode._7],
    ModifiedKey.asterisk: [KeyCode.left_shift, KeyCode._8],
    ModifiedKey.open_paren: [KeyCode.left_shift, KeyCode._9],
    ModifiedKey.close_paren: [KeyCode.left_shift, KeyCode._0],
    ModifiedKey.underscore: [KeyCode.left_shift, KeyCode.hyphen],
    ModifiedKey.plus_sign: [KeyCode.left_shift, KeyCode.equal_sign],
    ModifiedKey.open_curly: [KeyCode.left_shift, KeyCode.open_bracket],
    ModifiedKey.close_curly: [KeyCode.left_shift, KeyCode.close_bracket],
    ModifiedKey.colon: [KeyCode.left_shift, KeyCode.semicolon],
    ModifiedKey.double_quote: [KeyCode.left_shift, KeyCode.quote],
    ModifiedKey.pipe: [KeyCode.left_shift, KeyCode.backslash],
    ModifiedKey.tidle: [KeyCode.left_shift, KeyCode.grave_accent_and_tilde],
    ModifiedKey.less_than: [KeyCode.left_shift, KeyCode.comma],
    ModifiedKey.greater_than: [KeyCode.left_shift, KeyCode.period],
    ModifiedKey.question_mark: [KeyCode.left_shift, KeyCode.slash],
}


class Alias(BaseModel):
    pass


Key = KeyCode | ModifiedKey | Alias
Pos = tuple[int, int]


class KeyLayout(BaseModel):
    keys: dict[Pos, Key]
