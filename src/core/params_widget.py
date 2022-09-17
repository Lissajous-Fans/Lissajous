# TODO: Аннотации типов API

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QSpinBox

from src.core.param_field_widget import ParamFieldWidget
from src.core.param_group_widget import ParamGroupWidget
from src.api.plugins import (PluginOption,
                             PluginOptionGroup,
                             PluginOptionInt,
                             PluginOptionString,
                             PluginOptionBool,
                             PluginOptionComboBox)


def option_to_widget(option: PluginOption) -> tuple:
    type_to_match = type(option)
    match type_to_match:
        case x if isinstance(option, PluginOptionInt):
            w = QSpinBox()
            w.setRange(0, 100)
            return w, w.valueChanged
        case x if isinstance(option, PluginOptionBool):
            w = QSpinBox()
            w.setRange(0, 1)
            return w, w.valueChanged


class ParamsWidget(QListWidget):
    params_updated = pyqtSignal()

    def __init__(self, params: list[PluginOption | PluginOptionGroup]):
        super().__init__()
        self._params = params
        self._configure_ui()

    def _configure_ui(self):
        for param in self._params:
            if isinstance(param, PluginOption):
                self._fast_add(ParamFieldWidget(param.name, *option_to_widget(param)))
            elif isinstance(param, PluginOptionGroup):
                group = ParamGroupWidget(param.name)
                self._fast_add(group)
                for p in param.items:
                    w = ParamFieldWidget(p.name, *option_to_widget(p))
                    group.register_child(w)
                    self._fast_add(w)

    def _fast_add(self, widget: QWidget):
        item = QListWidgetItem(self)
        item.setSizeHint(widget.sizeHint())
        self.setItemWidget(item, widget)

