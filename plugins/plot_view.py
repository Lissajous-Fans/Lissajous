import pandas as pd
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtChart import QChart, QChartView, QLineSeries

from src.api.plugins import PluginQtVisualize, Plugin, VisualizeType


class PlotViewPlugin(PluginQtVisualize):
    def __init__(self):
        super().__init__(
            "Simple Line Graph View",
            "Line Graph View.",
            VisualizeType.LineGraph
        )

    def visualize(self, data: pd.DataFrame, params: Plugin.OptionsValues) -> QWidget:
        return QPushButton('asfdf')


__visual_plugins__ = [PlotViewPlugin]
__import_plugins__ = []
