import shared
from lushlayers.config import Config, Device

Config(
    device=Device(vendor_id=1452, product_id=591),
    aliases=shared.aliases,
    physical_layout=r"""
        esc  1    2    3    4    5    6    7    8    9    0    -    =    bspc
        tab  q    w    e    r    t    y    u    i    o    p    [    ]    \
        caps a    s    d    f    g    h    j    k    l    ;    '    ret
        lsft z    x    c    v    b    n    m    ,    .    /    rsft
        lctl lopt lcmd           spc            rcmd ropt fn   rctl
        """,
    layers=dict(
        default=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        @nav _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _              _              @sym _    _    _
        """,
        navigation=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _    del
        _    _    @cht @eml _    _    home @lwd @rwd end  _    _    _    _
        _    @mus @www @trm @doc _    left down up   rght _    _    _
        _    _    _    @vid @cal _    _    _    _    _    _    _
        _    _    _              _              _    _    _    _
        """,
        symbols=r"""
        _    _    _    _    _    _    _    _    rwnd pp   ff   vold volu _
        _    _    _    _    _    ~    _    _    _    _    _    _    _    _
        _    <    {    [    (    `    "    )    ]    }    >    _    _
        _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _              _              _    _    _    _
        """,
        __template=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _              _              _    _    _    _
        """,
    ),
)
