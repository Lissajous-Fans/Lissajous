from dataclasses import dataclass
from enum import Enum, auto
from io import BytesIO
from typing import Any, List, Optional, Tuple

from pandas import DataFrame


class PluginOptionType(Enum):
    INT = auto()
    FLOAT = auto()
    BOOL = auto()
    STRING = auto()
    COMBO_BOX = auto()
    COLOR = auto()


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
    def __init__(self, name: str, default_value: Tuple[int, int, int] = (0, 0, 0)):
        super().__init__(name, PluginOptionType.COLOR, default_value)


@dataclass
class PluginOptionGroup:
    name: str
    items: List[PluginOption]


class VisualizeMethod:
    pass


class Plugin:
    name: str
    description: str
    options: List[PluginOption | PluginOptionGroup]
    implicit_options: List[PluginOption]

    def __init__(self, name: str, description: str, options: List[PluginOption | PluginOptionGroup]):
        self.name = name
        self.description = description
        self.options = options
        self.implicit_options = []


class PluginImport(Plugin):
    def __init__(self, name: str, description: str):
        pass

    def import_from(self, file_path: str) -> DataFrame:
        pass


class VisualizeType(Enum):
    Map = auto()
    Diagram = auto()
    BarChart = auto()
    PieChart = auto()
    Table = auto()
    LineGraph = auto()
    Custom = auto()
    Undefined = auto()


class PluginVisualize(Plugin):
    def __init__(self):
        pass

    def visualize(self, data: DataFrame) -> BytesIO:
        pass
