import importlib
import os

import pandas as pd
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QAction, QMenu, QDockWidget)

from src.api.plugins import PluginVisualize, PluginImport
from .file_loader_dialog import FileLoaderDialog
from .navigation_widget import NavigationWidget
from .params_widget import ParamsWidget
from .visualizing_widget import VisualizingWidget


PLUGINS_FOLDER = './plugins/'
VISUAL_PLUGINS_CONTAINER = '__visual_plugins__'
IMPORT_PLUGINS_CONTAINER = '__import_plugins__'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._dataset: pd.DataFrame | None = None
        self._visual_plugins = []
        self._dataframes = []
        self._current_data: pd.DataFrame | None = None
        self._load_plugins()
        self._configure_ui()
        self._configure_menu()

    def _load_plugins(self):
        import_plugins = []
        visual_plugins = []
        for file in list(os.walk(PLUGINS_FOLDER))[0][2]:
            d = importlib.import_module(f'plugins.{file.rstrip(".py")}').__dict__
            import_plugins.extend(d[IMPORT_PLUGINS_CONTAINER])
            visual_plugins.extend(d[VISUAL_PLUGINS_CONTAINER])
        self._visual_plugins = list(map(lambda x: x(), visual_plugins))
        self._import_plugins = list(map(lambda x: x(), import_plugins))

    def _configure_menu(self):
        self.open_menu = self.file_menu.addMenu('Открыть')
        for imp in self._import_plugins:
            action = QAction(imp.name, self)
            action.triggered.connect(self._build_file_load_handler(imp))
            self.open_menu.addAction(action)

    def _configure_ui(self):
        uic.loadUi('./res/qt/main_window.ui', self)
        self.setWindowIcon(QIcon("./res/icon.png"))

        self.navigation_widget = NavigationWidget()
        self.navigation_widget.plugin_picked.connect(self._handle_plugin_picking)
        self.navigation_widget.dataframe_picked.connect(self._handle_file_picking)
        self.dock_navigation = QDockWidget('Навигация', self)
        self.dock_navigation.setWidget(self.navigation_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_navigation)
        # Table widget
        # Visual widget
        self.visualizing_widget = VisualizingWidget()
        self.setCentralWidget(self.visualizing_widget)
        # Params widget
        self.params_widgets = ParamsWidget()
        self.params_widgets.params_updated.connect(self._handle_params_updating)
        self.dock_params = QDockWidget('Параметры отрисовки', self)
        self.dock_params.setWidget(self.params_widgets)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_params)

    def _handle_file_adding(self, data: pd.DataFrame):
        self._dataframes.append(data)
        self._handle_file_picking(len(self._dataframes) - 1)

    def _handle_file_picking(self, index: int):
        print(index, self._dataframes)
        self._current_data = self._dataframes[index]
        self.navigation_widget.load_visual_plugins(self._visual_plugins)
        self.navigation_widget.load_dataframes(self._dataframes)

    def _build_file_load_handler(self, plugin: PluginImport):
        def handler():
            dialog = FileLoaderDialog(plugin)
            dialog.file_picked.connect(self._handle_file_adding)
            dialog.exec()
        return handler

    def _handle_plugin_picking(self, index: int):
        plugin = self._visual_plugins[index]
        self.params_widgets.set_params(plugin.parameters)
        self.visualizing_widget.set_plugin(plugin)
        self.visualizing_widget.set_params(self.params_widgets.get_params())
        self._handle_params_updating()

    def _handle_params_updating(self):
        self.visualizing_widget.set_params(self.params_widgets.get_params())
        self.visualizing_widget.visualize(self._current_data)
