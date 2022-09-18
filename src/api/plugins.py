import abc
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Tuple

from PyQt5.QtWidgets import QWidget
from pandas import DataFrame

from .options import *


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
    def import_from(
        self, file_path: str, parameters: Plugin.OptionsValues
    ) -> Optional[DataFrame]:
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

    def __init__(
        self,
        name: str,
        description: str,
        visualize_type: VisualizeType,
        export_formats: List[str] = [],
    ):
        super().__init__(name, description)
        self.visualize_type = visualize_type

    @abc.abstractmethod
    def visualize(
        self, data: DataFrame, parameters: Plugin.OptionsValues
    ) -> Optional[QWidget | Tuple[QWidget, Any]]:
        pass

    @abc.abstractmethod
    def export_to(
        self,
        file_path: str,
        data: DataFrame,
        visualized_data: Any,
        parameters: Plugin.OptionsValues,
    ) -> bool:
        pass


PluginQtVisualize = PluginVisualize
