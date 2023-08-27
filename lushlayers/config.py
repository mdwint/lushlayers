import inspect
import shlex
from pathlib import Path
from typing import Any, Self

from pydantic import BaseModel, Field, model_validator

from .keys import Alias, KeyCode
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
    hold: bool = True
    alone: str | None = None

    @model_validator(mode="after")
    def check(self) -> Self:
        if self.alone and not self.hold:
            raise ValueError("'alone' implies 'hold'")
        return self


class Combo(Alias):
    key: KeyCode
    modifiers: list[KeyCode]

    @classmethod
    def of(cls, descr: str) -> Self:
        *mods, key = (KeyCode(token) for token in descr.split())
        return cls(key=key, modifiers=mods)


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
