import shared
from lushlayers.config import Config, Device

# This keyboard is configured primarily through ZMK.
# It maps some keys to F-keys, which are mapped to apps here.
Config(
    device=Device(vendor_id=7504, product_id=24926),
    aliases=shared.aliases,
    physical_layout=r"""
        _    f19  f20  f21  _      _    _    _    _    _
        _    f22  f23  f24  _      _    _    _    _    _
        _    _    _    _    _      _    _    _    _    _
                       _    _      _    _
        """,
    layers=dict(
        default=r"""
        _    @cal @eml @mus _      _    _    _    _    _
        _    @cht @www @trm _      _    _    _    _    _
        _    _    _    _    _      _    _    _    _    _
                       _    _      _    _
        """,
        __template=r"""
        _    _    _    _    _      _    _    _    _    _
        _    _    _    _    _      _    _    _    _    _
        _    _    _    _    _      _    _    _    _    _
                       _    _      _    _
        """,
    ),
)
