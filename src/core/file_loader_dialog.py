import pandas as pd
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QLabel, QFileDialog

from .params_widget import ParamsWidget
from src.api import PluginOption, PluginImport


class FileLoaderDialog(QDialog):
    file_picked = pyqtSignal(pd.DataFrame)
    error = pyqtSignal()

    def __init__(self, plugin: PluginImport):
        super().__init__()
        self._plugin = plugin
        self._dataframe = None
        self._configure_ui()

    def _configure_ui(self):
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        if self._plugin.parameters:
            self._params_widget = ParamsWidget(self._plugin.parameters)
            self.grid.addWidget(self._params_widget, 0, 0, 1, 3)
        self._pick_label = QLabel('Файл не выбран')
        self.grid.addWidget(self._pick_label, 1, 0, 1, 2)
        self._file_picker_button = QPushButton('Выбрать файл')
        self._file_picker_button.clicked.connect(self._handle_file_picking)
        self.grid.addWidget(self._file_picker_button, 1, 2, 1, 1)

    def _handle_file_picking(self):
        file = QFileDialog.getOpenFileName(self, 'Выбор файла', filter=' '.join(self._plugin.supported_formats))[0]
        if file and (data := self._plugin.import_from(file, {})) is not None:
            self._dataframe = data
            self._pick_label.setText(f'Файл: {file}')
            self.file_picked.emit(self._dataframe)
            self.close()
        elif file:
            self.error.emit()
            self.close()
