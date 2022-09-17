from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QListWidget, QLabel

from src.core.params_widget import ParamsWidget


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._configure_ui()

    def _configure_ui(self):
        self.setWindowIcon(QIcon("/res/icon.png"))
        self.grid: QGridLayout = QGridLayout(self)
        self.setLayout(self.grid)
        self._plugins_label = QLabel('Диаграммы')
        self.grid.addWidget(self._plugins_label, 0, 0)
        self._plugins_list = QListWidget(self)
        self.grid.addWidget(self._plugins_list, 1, 0,)
        self._params_label = QLabel('Параметры отрисовки')
        self.grid.addWidget(self._params_label, 0, 1)
        self._params_widget = ParamsWidget([])
        self.grid.addWidget(self._params_widget, 1, 1,)
