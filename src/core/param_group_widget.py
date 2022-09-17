from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QWidget


class ParamGroupWidget(QStandardItem):
    param_updated = pyqtSignal()

    def __init__(self, name: str):
        super().__init__()
        self._name = name
        self._configure_ui()

    def _configure_ui(self):
        self.setText(self._name)
