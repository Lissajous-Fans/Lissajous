from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout


class ParamFieldWidget(QStandardItem):
    param_updated = pyqtSignal()

    def __init__(self, name: str, widget: QWidget, updater: pyqtSignal):
        super().__init__()
        self._name = name
        self._widget = widget
        self._updater = updater
        self._configure_ui()

    def _configure_ui(self):
        self.setText(self._name)
        self._updater.connect(self.param_updated.emit())
        self.setData(self._widget)
