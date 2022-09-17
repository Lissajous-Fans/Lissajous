import abc
from dataclasses import dataclass
from enum import Enum, auto
from io import BytesIO
from typing import Any, Dict, List, Optional, Tuple

from PyQt5.QtWidgets import QWidget
from pandas import DataFrame


class PluginOptionType(Enum):
    INT = auto()
    FLOAT = auto()
    BOOL = auto()
    STRING = auto()
    COMBO_BOX = auto()
    COLOR = auto()


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
    def __init__(self, name: str, default_value: Tuple[int, int, int] = (0, 0, 0)):
        super().__init__(name, PluginOptionType.COLOR, default_value)


@dataclass
class PluginOptionGroup:
    name: str
    items: List[PluginOption]


class Plugin:
    OptionsValues = Dict[PluginOption, Any]
    name: str
    description: str
    options: List[PluginOption | PluginOptionGroup]
    options_values: OptionsValues
    parameters: List[PluginOption | PluginOptionGroup]

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.options = []
        self.parameters = []


class PluginImport(Plugin):
    supported_formats: List[str]

    def __init__(self, name: str, description: str, supported_formats: List[str]):
        super().__init__(name, description)
        self.supported_formats = supported_formats

    @abc.abstractmethod
    def import_from(self, file_path: str, parameters: Plugin.OptionsValues) -> Optional[DataFrame]:
        """Import `DataFrame` from file at `file_path`self.
        Returns `None` if the file cannot be imported."""
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
    visualize_type: VisualizeType

    def __init__(self, name: str, description: str, visualize_type: VisualizeType):
        super().__init__(name, description)
        self.visualize_type = visualize_type

    @abc.abstractmethod
    def visualize(self, data: DataFrame, parameters: Plugin.OptionsValues) -> BytesIO:
        pass


class PluginQtVisualize(Plugin):
    visualize_type: VisualizeType

    def __init__(self, name: str, description: str, visualize_type: VisualizeType):
        super().__init__(name, description)
        self.visualize_type = visualize_type

    @abc.abstractmethod
    def visualize(self, data: DataFrame, parameters: Plugin.OptionsValues) -> QWidget:
        pass
