from typing import Callable

import pandas as pd
from PyQt5.QtCore import Qt, pyqtSignal, QSize, QModelIndex
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QDockWidget, QListWidget, QListWidgetItem

from core.plugin_item_widget import PluginItemWidget
from core.plugins_widget import PluginsWidget
from src.api import PluginQtVisualize


class NavigationWidget(QWidget):
    dataframe_picked = pyqtSignal(int)
    plugin_picked = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._data_list = []
        self._configure_ui()

    def _configure_ui(self):
        self.box = QVBoxLayout(self)
        self.setLayout(self.box)
        # Plugins label
        self._plugins_label = QLabel('Плагины визуализации:')
        self.layout().addWidget(self._plugins_label)
        # Plugins widget
        self._plugins_widget = PluginsWidget([])
        self.layout().addWidget(self._plugins_widget)
        # Dataset label
        self._data_label = QLabel('Наборы данных')
        self.layout().addWidget(self._data_label)
        # Dataset list
        self._data_widget = QListWidget(self)
        self._data_widget.clicked.connect(self._handle_data_frame_picking)
        self.box.addWidget(self._data_widget)

    def load_visual_plugins(self, plugins: list[Callable]):
        self._plugins_widget.clear()
        for i, plugin in enumerate(plugins):
            item = QListWidgetItem(self._plugins_widget)
            item.setSizeHint(QSize(100, 35))
            widget = PluginItemWidget(plugin, i)
            widget.clicked.connect(self._build_plugin_handler_picker(i))
            self._plugins_widget.setItemWidget(item, widget)

    def load_dataframes(self, dataframes: list[pd.DataFrame]):
        self._data_list = []
        self._data_widget.clear()
        for i, data in enumerate(dataframes):
            item = QListWidgetItem(f'Датасет №{i}', self._data_widget)
            item.setSizeHint(QSize(100, 35))
            self._data_widget.addItem(item)

    def _build_plugin_handler_picker(self, index: int):
        def handler():
            self.plugin_picked.emit(index)
        return handler

    def _handle_plugin_picking(self, index: int):
        self.plugin_picked.emit(index)

    def _handle_data_frame_picking(self, index: QModelIndex):
        self.dataframe_picked.emit(index.row())
