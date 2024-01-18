import shared
from lushlayers.config import Config, Device

Config(
    device=Device(vendor_id=1133, product_id=45915),
    aliases=shared.aliases,
    physical_layout=r"""
        esc  f1   f2   f3   f4   f5   f6   f7   f8   f9   f10  f11  f12  _    _    _    _    _    _    _    _
        nubs 1    2    3    4    5    6    7    8    9    0    -    =    bspc ins  home pgup nlck kp/  kp*  kp-
        tab  q    w    e    r    t    y    u    i    o    p    [    ]    ret  del  end  pgdn kp7  kp8  kp9  kp+
        caps a    s    d    f    g    h    j    k    l    ;    '    \                        kp4  kp5  kp6
        lsft `    z    x    c    v    b    n    m    ,    .    /         rsft      up        kp1  kp2  kp3
        lctl lopt lcmd                    spc                  rcmd fn   ropt left down rght      kp0  kp.  kprt
        """,
    layers=dict(
        default=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
        esc  _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
        @nav _    _    _    _    _    _    _    _    _    _    _    _                        _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _         _         _         _    _    _
        _    _    _              _              @sym _    _    _    _    _    _    _    _         _    _    _
        """,
        navigation=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    del  _    _    _    _    _    _    _
        _    _    @cht @eml _    _    home @lwd @rwd end  _    _    _    _    _    _    _    _    _    _    _
        _    @mus @www @trm @doc _    left down up   rght _    _    _                        _    _    _    _
        _    _    _    @vid @cal _    _    _    _    _    _    _         _         _         _    _    _
        _    _    _              _              _    _    _    _    _    _    _    _    _         _    _    _
        """,
        symbols=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    ~    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    <    {    [    (    `    "    )    ]    }    >    _    _                        _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _         _         _         _    _    _
        _    _    _              _              _    _    _    _    _    _    _    _    _         _    _    _
        """,
        __template=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _                        _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _         _         _         _    _    _
        _    _    _              _              _    _    _    _    _    _    _    _    _         _    _    _
        """,
    ),
)
