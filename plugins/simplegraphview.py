from lissapi import *
from io import BytesIO
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF


class SimpleLineGraphView(PluginQtVisualize):
    def __init__(self):
        super().__init__("Simple Line Graph View", "Line Graph View.", VisualizeType.LineGraph)

    def visualize(self, data: DataFrame, params: Plugin.ParametersValues) -> QWidget:
        series = QLineSeries()
        series.append(0, 6)
        series.append(3, 5)
        series.append(3, 8)
        series.append(7, 3)
        series.append(12, 7)
        series << QPointF(11,1) << QPointF(13,3) << QPointF(17,6) << QPointF(18,3) << QPointF(20,20)

        chart = QChart()
        addSeries(series)
        return QChartView(chart)


__plugins__ = [SimpleLineGraphView()]
