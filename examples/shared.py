from lushlayers.config import Combo, Open, Toggle

aliases = dict(
    nav=Toggle(layer="navigation", alone="bspc"),
    sym=Toggle(layer="symbols"),
    trm=Open(app="Alacritty"),
    www=Open(app="Vivaldi"),
    doc=Open(app="Dash"),
    mus=Open(app="Spotify"),
    cht=Open(app="Slack"),
    eml=Open(app="Mail"),
    cal=Open(app="Calendar"),
    vid=Open(app="zoom.us"),
    lwd=Combo.of("lopt left"),  # Move word left
    rwd=Combo.of("lopt rght"),  # Move word right
)
