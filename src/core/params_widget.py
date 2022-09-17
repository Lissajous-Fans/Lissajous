# TODO: Аннотации типов API

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QTreeView, QPushButton

from src.core.param_field_widget import ParamFieldWidget


class ParamsWidget(QTreeView):
    params_updated = pyqtSignal()

    def __init__(self, params: list[str]):
        super().__init__()
        self._params = params
        self._tree: QTreeView | None = None
        self._configure_ui()

    def _configure_ui(self):
        self.setHeaderHidden(True)
        self.header().setStretchLastSection(True)
        self._model = QStandardItemModel()
        self._root = self._model.invisibleRootItem()
        for
        for param in self._params:
            button = QPushButton('Push')
            self._add_param(param, button, button.clicked)
        self.expandAll()

    def _add_param(self, name: str, widget: QWidget, signal: pyqtSignal):


    def _add_group(self, name: str):
        self._current_group = QTreeWidgetItem(
            self,
            [name]
        )
        self.add
