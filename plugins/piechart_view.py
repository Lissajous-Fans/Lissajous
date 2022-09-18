from src.api import PluginVisualize, Plugin, VisualizeType
from pandas import DataFrame
from typing import Set
from PyQt5.QtWidgets import QWidget
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt


class PieChartViewPlugin(PluginVisualize):
    def __init__(self):
        super().__init__("Pie Chart View", "No description", VisualizeType.PieChart)

    @staticmethod
    def handle_howered(slice: QPieSlice, state: bool, checked_slices: Set[QPieSlice]):
        if state:
            slice.setExploded(True)
            slice.setLabelVisible(True)
        elif slice not in checked_slices:
            slice.setExploded(False)
            slice.setLabelVisible(False)

    @staticmethod
    def handle_click(slice, checked_splices: Set[QPieSlice]):
        if slice in checked_splices:
            checked_splices.remove(slice)
            slice.setPen(QPen(Qt.white, 0))
        else:
            checked_splices.add(slice)
            slice.setPen(QPen(Qt.black, 1))

    def visualize(self, data: DataFrame, params: Plugin.OptionsValues) -> QWidget:
        series = QPieSeries()
        for rx in range(1, data.shape[0]):
            series.append(data.iat[rx, 0], int(data.iat[rx, 1]))
        checked_slices: Set[QPieSlice] = set()
        series.hovered.connect(lambda slice, state: PieChartViewPlugin.handle_howered(slice, state, checked_slices))
        series.clicked.connect(lambda slice: PieChartViewPlugin.handle_click(slice, checked_slices))

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart Example")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        return chartview


__plugins__ = [PieChartViewPlugin()]
__visual_plugins__ = [PieChartViewPlugin]
__import_plugins__ = []
