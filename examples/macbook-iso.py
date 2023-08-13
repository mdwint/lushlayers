from lushlayers.config import Config, Device, Open, Toggle

Config(
    device=Device(vendor_id=1452, product_id=835),
    aliases=dict(
        nav=Toggle(layer="navigation"),
        sym=Toggle(layer="symbols"),
        trm=Open(app="Alacritty"),
        brw=Open(app="Vivaldi"),
        doc=Open(app="Dash"),
        mus=Open(app="Spotify"),
        cht=Open(app="Slack"),
        eml=Open(app="Mail"),
        cal=Open(app="Calendar"),
        vid=Open(app="zoom.us"),
    ),
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
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        @nav _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _              _              @sym _    _    _    _
        """,
        navigation=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    @cht @eml _    _    _    _    _    _    _    _    _    _
        _    @mus @brw @trm @doc _    left down up   rght _    _    _
        _    _    _    @vid @cal _    _    _    _    _    _    _    _    _
        _    _    _    _              _              _    _    _    _    _
        """,
        symbols=r"""
        _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
        _    _    _    _    _    _    _    _    _    _    _    _    _    _
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
