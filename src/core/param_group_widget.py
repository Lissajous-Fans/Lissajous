from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QLabel


class ParamGroupWidget(QLabel):
    clicked = pyqtSignal()

    def __init__(self, name: str):
        super().__init__()
        self._name = name
        self._opened = True
        self._children: list[QWidget] = []
        self._configure_ui()

    def _configure_ui(self):
        self.setText(f'{"∨" if self._opened else ">"} {self._name}')
        self.clicked.connect(self._handle_click)
        self.setMinimumHeight(40)

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.clicked.emit()

    def _handle_click(self):
        self._opened = not self._opened
        self.setText(f'{"∨" if self._opened else ">"} {self._name}')
        for x in self._children:
            x.setVisible(self._opened)

    def register_child(self, widget: QWidget):
        self._children.append(widget)
