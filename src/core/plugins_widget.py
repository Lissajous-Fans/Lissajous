from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from src.api import Plugin, PluginVisualize
from .plugin_item_widget import PluginItemWidget


class PluginsWidget(QListWidget):
    plugin_picked = pyqtSignal(int)

    def __init__(self, plugins: list[PluginVisualize]):
        super().__init__()
        print(plugins)
        self._plugins = plugins
        self._configure_ui()

    def _configure_ui(self):
        for i, plugin in enumerate(self._plugins):
            self.add_plugin(plugin, i)

    def add_plugin(self, plugin: PluginVisualize, index: int):
        item = QListWidgetItem(self)
        widget = PluginItemWidget(plugin, index)
        widget.clicked.connect(self._handle_plugin_picking)
        item.setSizeHint(widget.sizeHint())
        self.setItemWidget(item, widget)

    def _handle_plugin_picking(self, plugin_id: int):
        self.plugin_picked.emit(plugin_id)
