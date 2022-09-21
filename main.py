import sys

from PyQt5.QtWidgets import QApplication

from src.core.main_window import MainWindow


def enable_threads_exceptions() -> None:
    """
    Включает прослушивание исключений из сторонних потоков.
    Необходимо для отладки PyQt.
    """
    excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook


def main():
    enable_threads_exceptions()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
