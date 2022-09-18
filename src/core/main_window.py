import importlib
import os

import pandas as pd
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QAction, QMenuBar)

from .main_widget import MainWidget
from src.api.plugins import PluginVisualize, PluginImport
from .file_loader_dialog import FileLoaderDialog

PLUGINS_FOLDER = './plugins/'
VISUAL_PLUGINS_CONTAINER = '__visual_plugins__'
IMPORT_PLUGINS_CONTAINER = '__import_plugins__'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._dataset: pd.DataFrame | None = None
        self._plugins = []
        self._configure_ui()

    def _configure_ui(self):
        uic.loadUi('./res/qt/main_window.ui', self)
        self.setWindowIcon(QIcon("./res/icon.png"))

        self.setMenuBar(QMenuBar(self))
        self.file_menu = self.menuBar().addMenu('Файл')
        self.open_menu = self.file_menu.addMenu('Открыть')

        visual_plugins = self.load_plugins_by_type(VISUAL_PLUGINS_CONTAINER)
        for plugin in visual_plugins:
            self._plugins.append(plugin())

        import_plugins = self.load_plugins_by_type(IMPORT_PLUGINS_CONTAINER)
        for plugin in import_plugins:
            plugin = plugin()
            action = QAction(plugin.name, self)
            action.triggered.connect(lambda: self._load_file(plugin))
            self.open_menu.addAction(action)

    def load_plugins_by_type(self, plugin_type: str) -> list:
        files = list(os.walk(PLUGINS_FOLDER))[0][2]
        result = []
        for file in files:
            if file.endswith('.py'):
                result.extend(importlib.import_module(f'plugins.{file.removesuffix(".py")}').__dict__[plugin_type])
        return result

    def _handle_file_picking(self, data: pd.DataFrame):
        self._dataset = data
        self.setCentralWidget(MainWidget(self._dataset, self._plugins))

    def _load_file(self, plugin: PluginImport):
        dialog = FileLoaderDialog(plugin)
        dialog.file_picked.connect(self._handle_file_picking)
        dialog.exec()
