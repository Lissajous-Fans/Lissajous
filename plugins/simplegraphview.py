from lissapi import *
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF

from pandas import DataFrame


class SimpleLineGraphView(PluginQtVisualize):
    def __init__(self):
        super().__init__("Simple Line Graph View", "Line Graph View.", VisualizeType.LineGraph)
        self.param_color = PluginOptionColor("Color Param", (200, 0, 0))
        self.param_string = PluginOptionString("String Param", "default string")
        self.param_bool = PluginOptionBool("Bool Param")
        self.param_int = PluginOptionInt("Int param", 64, 0, 200)
        self.param_float = PluginOptionFloat("Float param", 5.3, -1.0, 6.0)
        self.parameters = [
            self.param_color,
            PluginOptionGroup(name="Option Group",
                              items=[
                                  self.param_int,
                                  self.param_color,
                                  self.param_float
                              ]),
            self.param_string,
            self.param_bool
        ]

    def visualize(self, data: DataFrame, params: Plugin.OptionsValues) -> QWidget:
        label_x, label_y = data.head()

        series = QLineSeries()
        chart = QChart()
        return QChartView(chart)


__plugins__ = [SimpleLineGraphView()]
