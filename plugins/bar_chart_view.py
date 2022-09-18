import pandas as pd
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColorConstants, QColor, QPen
from PyQt5.QtWidgets import QWidget, QPushButton, QGraphicsSceneMouseEvent, QColorDialog
from PyQt5.QtChart import QChart, QChartView, QLineSeries
import pyqtgraph as pg

from src.api import PluginVisualize, Plugin, VisualizeType, PluginOptionInt


class BarChartPlugin(PluginVisualize):
    def __init__(self):
        super().__init__(
            "Simple Bar Chart View",
            "Bar chart View.",
            VisualizeType.BarChart
        )
        self.param_x_min = PluginOptionInt("Left column", 1)
        self.param_x_max = PluginOptionInt("Right Column", 3)
        self.param_y_min = PluginOptionInt("Top row", 1)
        self.param_y_max = PluginOptionInt("Bottom row", 5)
        self.parameters.extend([self.param_x_min, self.param_y_min, self.param_y_max, self.param_x_min])

    def visualize(self, data: pd.DataFrame, params: Plugin.OptionsValues) -> QWidget:
        plot = pg.plot()
        # create list for y-axis
        y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
        # create horizontal list i.e x-axis
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # create pyqt5graph bar graph item
        # with width = 0.6
        # with bar colors = green
        bargraph = pg.BarGraphItem(x=x, height=y1, width=0.6, brush='g')
        # add item to plot window
        # adding bargraph item to the plot window
        plot.addItem(bargraph)
        return plot


__visual_plugins__ = [BarChartPlugin]
__import_plugins__ = []
