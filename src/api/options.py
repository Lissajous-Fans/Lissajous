from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, List, Optional

from PyQt5.QtGui import QColor


class PluginOptionType(Enum):
    INT = auto()
    FLOAT = auto()
    BOOL = auto()
    STRING = auto()
    COMBO_BOX = auto()
    COLOR = auto()
    CUSTOM = auto()


@dataclass
class PluginOption:
    name: str
    option_type: PluginOptionType
    default_value: Any

    def __hash__(self) -> int:
        return hash(self.name)


class PluginOptionBool(PluginOption):
    def __init__(self, name: str, default_value: bool = False):
        super().__init__(name, PluginOptionType.BOOL, default_value)


class PluginOptionInt(PluginOption):
    min_value: Optional[int]
    max_value: Optional[int]

    def __init__(self, name: str, default_value: int = 0,
                 min_value: Optional[int] = None,
                 max_value: Optional[int] = None):
        super().__init__(name, PluginOptionType.INT, default_value)
        self.min_value = min_value
        self.max_value = max_value


class PluginOptionFloat(PluginOption):
    min_value: Optional[float]
    max_value: Optional[float]

    def __init__(self, name: str, default_value: float = 0,
                 min_value: Optional[float] = None,
                 max_value: Optional[float] = None):
        super().__init__(name, PluginOptionType.FLOAT, default_value)
        self.min_value = min_value
        self.max_value = max_value


class PluginOptionString(PluginOption):
    def __init__(self, name: str, default_value: str = ""):
        super().__init__(name, PluginOptionType.STRING, default_value)


class PluginOptionComboBox(PluginOption):
    items: List[str]

    def __init__(self, name: str, items: List[str], default_value: Optional[str] = None):
        super().__init__(name, PluginOptionType.COMBO_BOX, default_value)
        self.items = items


class PluginOptionColor(PluginOption):
    def __init__(self, name: str, default_value: QColor = QColor(0, 0, 0)):
        super().__init__(name, PluginOptionType.COLOR, default_value)


@dataclass
class PluginOptionGroup:
    name: str
    items: List[PluginOption]
