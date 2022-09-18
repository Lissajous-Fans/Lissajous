import pandas as pd
from PyQt5.QtWidgets import QWidget, QSplitter, QHBoxLayout, QGridLayout

from src.api import PluginQtVisualize


class VisualizingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._plugin: PluginQtVisualize | None = None
        self._params: dict = {}
        self.widget = QWidget()
        self.setLayout(QGridLayout(self))

    def set_params(self, params: dict):
        self._params = params

    def set_plugin(self, plugin: PluginQtVisualize):
        self._plugin = plugin

    def visualize(self, data: pd.DataFrame):
        try:
            self.widget = self._plugin.visualize(data, self._params)
            self.layout().addWidget(self.widget, 0, 0)
        except Exception as e:
            print(e)
