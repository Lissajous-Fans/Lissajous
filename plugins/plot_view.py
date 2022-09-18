import pandas as pd
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColorConstants, QColor, QPen
from PyQt5.QtWidgets import QWidget, QPushButton, QGraphicsSceneMouseEvent, QColorDialog
from PyQt5.QtChart import QChart, QChartView, QLineSeries

from src.api.plugins import PluginQtVisualize, Plugin, VisualizeType, PluginOptionInt


class PlotViewPlugin(PluginQtVisualize):
    def __init__(self):
        super().__init__(
            "Simple Line Graph View",
            "Line Graph View.",
            VisualizeType.LineGraph
        )
        self.param_x_min = PluginOptionInt("Left Row", 0)
        self.param_y_min = PluginOptionInt("Top Column", 0)
        self.param_y_max = PluginOptionInt("Bottom Column", 0)
        self.parameters.extend([self.param_x_min, self.param_y_min, self.param_y_max])

    def visualize(self, data: pd.DataFrame, params: Plugin.OptionsValues) -> QWidget:
        print(data)
        series = QLineSeries()
        x = params[self.param_x_min]
        for y in range(params[self.param_y_min], params[self.param_y_max] + 1):
            series.append(data[x][y], data[x + 1][y])
        series.clicked.connect(lambda: series.setColor(QColorDialog().getColor()))
        chart = QChart()
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle("Just Title")
        view = QChartView(chart)
        return view


__visual_plugins__ = [PlotViewPlugin]
__import_plugins__ = []
