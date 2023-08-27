from typing import Annotated, Literal

from pydantic import BaseModel, Field

from .config import Combo, Config, Device, Open, Shell, Toggle
from .keys import KeyCode, KeyLayout, ModifiedKey


class DeviceIf(BaseModel):
    type: Literal["device_if"] = "device_if"
    identifiers: list[Device]


class VariableIf(BaseModel):
    type: Literal["variable_if"] = "variable_if"
    name: str
    value: str | int


Condition = Annotated[
    DeviceIf | VariableIf,
    Field(discriminator="type"),
]


class KeyFrom(BaseModel):
    key_code: str


class SetVariable(BaseModel):
    name: str
    value: str | int


class KeyTo(BaseModel):
    key_code: str | None = None
    modifiers: list[str] | None = None
    shell_command: str | None = None
    set_variable: SetVariable | None = None


class Manipulator(BaseModel):
    type: Literal["basic"] = "basic"
    conditions: list[Condition]
    from_: KeyFrom = Field(serialization_alias="from")
    to: list[KeyTo]
    to_after_key_up: list[KeyTo] | None = None
    to_if_alone: list[KeyTo] | None = None


class Rule(BaseModel):
    description: str
    manipulators: list[Manipulator]


class KarabinerConfig(BaseModel):
    title: str
    rules: list[Rule]


def render_config(
    config: Config, layout: KeyLayout, layers: dict[str, KeyLayout]
) -> None:
    if_device = DeviceIf(identifiers=[config.device])
    manipulators = []

    for layer_name, layer in layers.items():
        if_layer = VariableIf(
            name="layer", value=0 if layer_name == "default" else layer_name
        )

        for pos, key_to in layer.keys.items():
            key_from = layout.keys[pos]
            assert isinstance(key_from, KeyCode)

            if isinstance(key_to, Open):
                key_to = key_to.to_shell()

            if isinstance(key_to, KeyCode):
                manip = Manipulator(
                    conditions=[if_device, if_layer],
                    from_=KeyFrom(key_code=key_from.code),
                    to=[KeyTo(key_code=key_to.code)],
                )
            elif isinstance(key_to, ModifiedKey):
                *mods, key_to = key_to.combination
                manip = Manipulator(
                    conditions=[if_device, if_layer],
                    from_=KeyFrom(key_code=key_from.code),
                    to=[KeyTo(key_code=key_to.code, modifiers=[m.code for m in mods])],
                )
            elif isinstance(key_to, Combo):
                manip = Manipulator(
                    conditions=[if_device, if_layer],
                    from_=KeyFrom(key_code=key_from.code),
                    to=[
                        KeyTo(
                            key_code=key_to.key.code,
                            modifiers=[m.code for m in key_to.modifiers],
                        )
                    ],
                )
            elif isinstance(key_to, Shell):
                manip = Manipulator(
                    conditions=[if_device, if_layer],
                    from_=KeyFrom(key_code=key_from.code),
                    to=[KeyTo(shell_command=key_to.cmd)],
                )
            elif isinstance(key_to, Toggle):
                on = SetVariable(name="layer", value=key_to.layer)
                off = SetVariable(name="layer", value=0)
                manip = Manipulator(
                    conditions=[if_device, if_layer],
                    from_=KeyFrom(key_code=key_from.code),
                    to=[KeyTo(set_variable=on)],
                )
                if key_to.hold:
                    manip.to_after_key_up = [KeyTo(set_variable=off)]
                    alone = KeyCode(key_to.alone) if key_to.alone else key_from
                    manip.to_if_alone = [KeyTo(key_code=alone.code)]
            else:
                print(f"WARNING: Not implemented: {key_to}")
                continue

            manipulators.append(manip)

    title = f"lushlayers-{config._path.stem}"
    cfg = KarabinerConfig(
        title=title, rules=[Rule(description=title, manipulators=manipulators)]
    )
    out = cfg.model_dump_json(indent=2, by_alias=True, exclude_none=True)

    out_path = config._path.with_suffix(".json")
    out_path.write_text(out)
    print(f"Wrote {out_path}")
