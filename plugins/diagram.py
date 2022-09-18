from PyQt5.QtCore import QModelIndex

from src.api.plugins import PluginQtVisualize, Plugin, VisualizeType
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
            "Table display",
            "No description",
            VisualizeType.PieChart
        )

    @staticmethod
    def handle_howered (slice, state):
        if state:
            slice.setExploded(True)
            slice.setLabelVisible(True)
        else:
            slice.setExploded(False)
            slice.setLabelVisible(False)

    def visualize(self, data: DataFrame, params: Plugin.OptionsValues) -> QWidget:
        series = QPieSeries()
        series.append("Python", 80)
        series.append("C++", 70)
        series.append("Java", 50)
        series.append("C#", 40)
        series.append("PHP", 30)
        series.hovered.connect(DiagramViewPlugin.handle_howered)
        
        
        slice = QPieSlice()
        slice = series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 2))
        slice.setBrush(Qt.green)
 
 
 
 
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
