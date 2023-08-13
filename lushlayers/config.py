import inspect
import shlex
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from .keys import Alias
from .parser import parse_key_layout


class Device(BaseModel):
    vendor_id: int
    product_id: int


class Shell(Alias):
    cmd: str


class Open(Alias):
    app: str

    def to_shell(self) -> Shell:
        return Shell(cmd=shlex.join(["open", "-a", self.app]))


class Toggle(Alias):
    layer: str


class Config(BaseModel):
    _path: Path
    device: Device
    physical_layout: str
    aliases: dict[str, Alias] = Field(default_factory=dict)
    layers: dict[str, str] = Field(default_factory=dict)

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self._path = Path(inspect.stack()[1].filename)
        _register(self)


def _register(config: Config) -> None:
    from .karabiner import render_config

    layout = parse_key_layout(config.physical_layout, aliases={})
    layers = {
        name: parse_key_layout(layer, config.aliases)
        for name, layer in config.layers.items()
        if name != "__template"
    }
    render_config(config, layout, layers)
