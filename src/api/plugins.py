from typing import Any, List, Optional
from enum import Enum, IntFlag
from dataclasses import dataclass


class PluginOptionType(Enum):
    INT = 1,
    BOOL = 2,
    STRING = 3,
    COMBO_BOX = 4


class PluginOption:
    name: str
    option_type: PluginOptionType
    default_value: Any
    value: Any

    def __init__(self, name: str, option_type: PluginOptionType, default_value: Optional[Any]):
        self.name = name
        self.option_type = option_type
        self.dafault_value = default_value
        self.value = self.default_value


class PluginOptionBool(PluginOption):
    def __init__(self, name: str, default_value: bool = False):
        super().__init__(name, PluginOptionType.BOOL, default_value)

    def __bool__(self):
        return self.value


class PluginOptionInt(PluginOption):
    class Hints(IntFlag):
        ANY = 0
        POSITIVE = 1

    hints: Hints

    def __init__(self, name: str, default_value: int = 0, hints: Hints = Hints.ANY):
        super().__init__(name, PluginOptionType.INT, default_value)
        self.hints = hints


class PluginOptionString(PluginOption):
    def __init__(self, name: str, default_value: str = ""):
        super().__init__(name, PluginOptionType.STRING, default_value)


class PluginOptionComboBox(PluginOption):
    items: List[str]

    def __init__(self, name: str, items: List[str], default_value: Optional[str] = None):
        super().__init__(name, PluginOptionType.COMBO_BOX, default_value)
        self.items = items


@dataclass
class PluginOptionGroup:
    name: str
    items: List[PluginOption]


class VisualizeMethod:
    pass


class Plugin:
    name: str
    decription: str
    options: List[PluginOption | PluginOptionGroup]

    def __init__(self, name: str, description: str, options: List[PluginOption | PluginOptionGroup]):
        self.name = name
        self.decription = description
        self.options = options


class PluginImport(Plugin):
    pass


class PluginVisualize(Plugin):
    pass


class PluginData(Plugin):
    pass
