import io

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class CanvasWidget(QLabel):
    def __init__(self):
        super().__init__()
        self._image: io.BytesIO | None = None
        self._configure_ui()

    def _configure_ui(self):
        pass

    def set_image(self, image: io.BytesIO):
        self.setPixmap(QPixmap().loadFromData(image))

    def get_image(self) -> io.BytesIO:
        return self._image
