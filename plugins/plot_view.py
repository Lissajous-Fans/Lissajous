import pandas as pd
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtChart import QChart, QChartView, QLineSeries

from src.api import PluginQtVisualize, Plugin, VisualizeType


class PlotViewPlugin(PluginQtVisualize):
    def __init__(self):
        super().__init__(
            "Simple Line Graph View",
            "Line Graph View.",
            VisualizeType.LineGraph
        )

    def visualize(self, data: pd.DataFrame, params: Plugin.OptionsValues) -> QWidget:
        series = QLineSeries()
        series << QPointF(0.0, 1.0) << QPointF(2.0, 3.0) << QPointF(4.0, -1.0)
        chart = QChart()
        chart.addSeries(series)
        # chart.createDefaultAxes()
        chart.setTitle("Just title")
        return QChartView(chart)


__visual_plugins__ = [PlotViewPlugin]
__import_plugins__ = []
