from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QGridLayout, QListWidget

from src.core.params_widget import ParamsWidget

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._configure_ui()

    def _configure_ui(self):
        self.setLayout(QGridLayout(self))
        self.grid: QGridLayout = self.layout()
        self._plugins_list = QListWidget(self)
        self.grid.addWidget(self._plugins_list, 0, 0,)
        self._params_widget = ParamsWidget(["Первый, второй, тритий"])
        self.grid.addWidget(self._params_widget, 0, 1,)
