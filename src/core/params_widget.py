# TODO: Аннотации типов API

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QWidget,
    QListWidget,
    QListWidgetItem,
    QSpinBox,
    QLineEdit,
    QVBoxLayout,
    QLabel,
    QDockWidget,
    QPushButton,
    QColorDialog,
)
from PyQt5.QtGui import QColor, QPalette

from src.api.plugins import (
    PluginOption,
    PluginOptionGroup,
    PluginOptionInt,
    PluginOptionBool,
    PluginOptionString,
    PluginOptionColor,
)
from .param_item_widget import ParamItemWidget
from .param_group_widget import ParamGroupWidget


class ColorInput(QPushButton):
    valueChanged = pyqtSignal(QColor)

    def __init__(self, color: QColor, parent=None):
        super().__init__("", parent)
        self.setAutoFillBackground(True)
        self.setColor(color)
        self.clicked.connect(lambda: self.setColor(QColorDialog().getColor()))

    def setColor(self, color: QColor):
        self.color = color
        pal = self.palette()
        pal.setColor(QPalette.Button, color)
        self.setPalette(pal)
        self.update()
        self.valueChanged.emit(self.value())

    def value(self) -> QColor:
        return self.color


def option_to_widget(option: PluginOption) -> tuple:
    type_to_match = type(option)
    match type_to_match:
        case x if isinstance(option, PluginOptionInt):
            w = QSpinBox()
            w.setRange(0, 100)
            return w, w.valueChanged, w.value
        case x if isinstance(option, PluginOptionBool):
            w = QSpinBox()
            w.setRange(0, 1)
            return w, w.valueChanged, lambda: bool(w.value())
        case x if isinstance(option, PluginOptionString):
            w = QLineEdit()
            return w, w.textChanged, w.text
        case x if isinstance(option, PluginOptionColor):
            w = ColorInput(option.default_value)
            return w, w.valueChanged, w.value
        case x if isinstance(option, PluginOptionFloat):
            pass
        case _:
            print(type_to_match)


class ParamsWidget(QWidget):
    params_updated = pyqtSignal()

    def __init__(self, params: list[PluginOption | PluginOptionGroup] = None):
        super().__init__()
        self._params = params or []
        self._params_to_widget = {}
        self._params_to_value_getter = {}
        self._configure_ui()

    def _configure_ui(self):
        self.box = QVBoxLayout(self)
        self.setLayout(self.box)
        # List
        self.list = QListWidget(self)
        self.box.addWidget(self.list)
        # Set params
        self.set_params(self._params)
        self.adjustSize()

    def set_params(self, params: list[PluginOption | PluginOptionGroup]):
        assert isinstance(PluginOptionColor("name", QColor()), PluginOption)
        self._params = params
        for param in self._params:
            print(param)
            if isinstance(param, PluginOption):
                print(2)
                self._fast_add_param(param)
            elif isinstance(param, PluginOptionGroup):
                group = ParamGroupWidget(param.name)
                self._fast_add(group)
                for sub_param in param.items:
                    self._fast_add_param(sub_param)
                    group.register_child(self._params_to_widget[sub_param])

    def drop_params(self):
        print("Dropping params.")
        self._params = []
        self._params_to_widget.clear()
        self._params_to_value_getter.clear()
        self.list.clear()

    def get_params(self):
        print(self._params)
        print(self._params_to_value_getter)
        return {param: self._params_to_value_getter[param]() for param in self._params}

    def _handle_param_updating(self, *args, **kwargs):
        self.params_updated.emit()

    def _fast_add_param(self, param: PluginOption):
        widget, callback, get_value = option_to_widget(param)
        widget = ParamItemWidget(param.name, widget, callback)
        self._params_to_value_getter[param] = get_value
        self._params_to_widget[param] = widget
        callback.connect(self._handle_param_updating)
        self._fast_add(widget)

    def _fast_add(self, widget: QWidget):
        item = QListWidgetItem(self.list)
        item.setSizeHint(widget.sizeHint())
        self.list.setItemWidget(item, widget)
