from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel

from src.api.plugins import PluginVisualize


class PluginItemWidget(QWidget):
    clicked = pyqtSignal(int)

    def __init__(self, plugin: PluginVisualize, index: int):
        super().__init__()
        self._index = index
        self._plugin = plugin
        self._configure_ui()

    def _configure_ui(self):
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self._label = QLabel(self._plugin.name)
        self.grid.addWidget(self._label, 0, 0)

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        self.clicked.emit(self._index)
