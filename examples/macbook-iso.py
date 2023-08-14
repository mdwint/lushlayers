import shared
from lushlayers.config import Config, Device

Config(
    device=Device(vendor_id=1452, product_id=835),
    aliases=shared.aliases,
    physical_layout=r"""
        esc  f1   f2   f3   f4   f5   f6   f7   f8   f9   f10  f11  f12
        nubs 1    2    3    4    5    6    7    8    9    0    -    =    bspc
        tab  q    w    e    r    t    y    u    i    o    p    [    ]    ret
        caps a    s    d    f    g    h    j    k    l    ;    '    \
        lsft `    z    x    c    v    b    n    m    ,    .    /    up   rsft
        fn   lctl lopt lcmd           spc            rcmd ropt left down rght
        """,
    layers=dict(
        default=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _
        esc  _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        @nav _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _              _              @sym _    _    _    _
        """,
        navigation=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    @cht @eml _    _    home @lwd @rwd end  _    _    _    _
        _    @mus @www @trm @doc _    left down up   rght _    _    _
        _    _    _    @vid @cal _    _    _    _    _    _    _    _    _
        _    _    _    _              _              _    _    _    _    _
        """,
        symbols=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    ~    _    _    _    _    _    _    _    _
        _    <    {    [    (    `    "    )    ]    }    >    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _              _              _    _    _    _    _
        """,
        __template=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _              _              _    _    _    _    _
        """,
    ),
)
