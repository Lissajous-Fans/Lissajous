from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout


class ParamItemWidget(QWidget):
    param_updated = pyqtSignal()

    def __init__(self, name: str, widget: QWidget, updater: pyqtSignal):
        super().__init__()
        self._name = name
        self._widget = widget
        self._updater = updater
        self._configure_ui()

    def _configure_ui(self):
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self._label = QLabel(self._name)
        self.grid.addWidget(self._label, 0, 0)
        self.grid.addWidget(self._widget, 0, 1)
        self.param_updated.connect(self._updater.emit)

