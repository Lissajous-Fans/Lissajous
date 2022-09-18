import pandas as pd
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColorConstants, QColor, QPen
from PyQt5.QtWidgets import QWidget, QPushButton, QGraphicsSceneMouseEvent, QColorDialog
from PyQt5.QtChart import QChart, QChartView, QLineSeries

from src.api import PluginVisualize, Plugin, VisualizeType, PluginOptionInt


class PlotViewPlugin(PluginVisualize):
    def __init__(self):
        super().__init__(
            "Simple Line Graph View",
            "Line Graph View.",
            VisualizeType.LineGraph
        )
        self.param_x_min = PluginOptionInt("Left column", 0)
        self.param_x_max = PluginOptionInt("Right Column", 0)
        self.param_y_min = PluginOptionInt("Top row", 0)
        self.param_y_max = PluginOptionInt("Bottom row", 0)
        self.parameters.extend([self.param_x_min, self.param_y_min, self.param_y_max, self.param_x_min])

    def visualize(self, data: pd.DataFrame, params: Plugin.OptionsValues) -> QWidget:
        print(data)
        params[self.param_x_min] = 0
        params[self.param_x_max] = 1
        params[self.param_y_min] = 0
        params[self.param_y_max] = 16

        series = QLineSeries()
        x0 = params[self.param_x_min]
        for y in range(params[self.param_y_min], params[self.param_y_max] + 1):
            print('add', (data[x0][y], data[x0 + 1][y]))
            series.append(data[x0][y], data[x0 + 1][y])

        series.clicked.connect(lambda: series.setColor(QColorDialog().getColor()))
        chart = QChart()
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle("Just Title")
        view = QChartView(chart)
        return view



__plugins__ = [PlotViewPlugin()]
__visual_plugins__ = [PlotViewPlugin]
__import_plugins__ = []
