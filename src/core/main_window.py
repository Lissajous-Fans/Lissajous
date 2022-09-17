from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow)

from src.core.main_widget import MainWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._configure_ui()

    def _configure_ui(self):
        uic.loadUi('./res/qt/main_window.ui', self)
        self.setWindowIcon(QIcon("./res/icon.png"))
        self.setCentralWidget(MainWidget())
