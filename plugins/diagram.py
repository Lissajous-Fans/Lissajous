from PyQt5.QtCore import QModelIndex

from lissapi import PluginQtVisualize, Plugin, VisualizeType
import pandas as pd
from PyQt5.QtWidgets import QWidget, QTableView
from PyQt5 import QtCore
from pandas import DataFrame

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class DiagramViewPlugin(PluginQtVisualize):
    def __init__(self):
        super().__init__(
            "Pie Charm",
            "No description",
            VisualizeType.PieChart
        )

    setExplodet = {}

    @staticmethod
    def handle_howered (slice, state):
        if state:
            slice.setExploded(True)
            slice.setLabelVisible(True)
        else:
            if not slice in DiagramViewPlugin.setExplodet:
                slice.setExploded(False)
                slice.setLabelVisible(False)
    
    @staticmethod
    def handle_click (slice):
        if slice in DiagramViewPlugin.setExplodet:
            DiagramViewPlugin.setExplodet.pop(slice)
            slice.setPen(QPen(Qt.white, 0))
        else:
            DiagramViewPlugin.setExplodet[slice] = 0
            slice.setPen(QPen(Qt.black, 1))

    def visualize(self, data: DataFrame, params: Plugin.OptionsValues) -> QWidget:
        series = QPieSeries()
        for rx in range(1, data.shape[0]):
            series.append(data.iat[rx, 0], int(data.iat[rx, 1]))
        series.hovered.connect(DiagramViewPlugin.handle_howered)
        series.clicked.connect(DiagramViewPlugin.handle_click)
 
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
        

__visual_plugins__ = [DiagramViewPlugin]
__import_plugins__ = []
