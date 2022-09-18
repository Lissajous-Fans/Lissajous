import pandas as pd
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QListWidget, QLabel

from .plugins_widget import PluginsWidget
from .params_widget import ParamsWidget
from src.api.plugins import Plugin, PluginVisualize


class MainWidget(QWidget):
    def __init__(self, data: pd.DataFrame, plugins: list[PluginVisualize] = None):
        super().__init__()
        self._data = data
        self._plugins = plugins or []
        self._current_plugin: PluginVisualize | None = None
        self._configure_ui()

    def _configure_ui(self):
        self.setWindowIcon(QIcon("/res/icon.png"))
        self.grid: QGridLayout = QGridLayout(self)
        self.setLayout(self.grid)

        self._plugins_label = QLabel('Диаграммы')
        self.grid.addWidget(self._plugins_label, 0, 0)
        self._plugins_list = PluginsWidget(self._plugins)
        self._plugins_list.plugin_picked.connect(self._handle_plugin_picking)
        self.grid.addWidget(self._plugins_list, 1, 0)

        self._params_label = QLabel('Параметры отрисовки')
        self.grid.addWidget(self._params_label, 0, 1)
        self._params_widget = ParamsWidget([])
        self.grid.addWidget(self._params_widget, 1, 1, )

        self._image_label = QLabel()
        self.grid.addWidget(self._image_label, 0, 2)

    def _handle_plugin_picking(self, plugin_id: int):
        self._params_widget.drop_params()
        self._current_plugin = self._plugins[plugin_id]
        self._params_widget.load_params(self._current_plugin.parameters)
        self._params_widget.params_updated.connect(lambda: self._update_visual(self._current_plugin))
        self._update_visual(self._current_plugin)

    def _update_visual(self, plugin: PluginVisualize):
        buffer = plugin.visualize(self._data, self._params_widget.get_params())
        self._image_label.setPixmap(QPixmap().loadFromData(buffer))

    def set_pixmap(self, image: QPixmap):
        self._image_label.setPixmap(image)
