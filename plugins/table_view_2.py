from pandas import DataFrame
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtWidgets import QTableView, QWidget

from src.api import Plugin, PluginVisualize, VisualizeType


class DataFrameWidget(QAbstractTableModel):
    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class TableViewPlugin(PluginVisualize):
    def __init__(self):
        super().__init__(
            "Table View", "No description.", VisualizeType.Table, ["*.csv", "*.xlsx"]
        )
        self.param_sort_by = 1
        self.parameters = []

    def visualize(self, data: DataFrame, params: Plugin.OptionsValues) -> QWidget:
        table_view = QTableView()
        table_view.setModel(DataFrameWidget(data))
        return table_view


__plugins__ = [TableViewPlugin()]
