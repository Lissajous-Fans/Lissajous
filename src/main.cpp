#include <QApplication>

#include "ui/mainwindow.h"

int main(int argc, char** args) {
    new QApplication(argc, args);
    QApplication::setApplicationName("Lissajous");
    QApplication::setOrganizationName("Lissajous-Fans");
    QApplication::setWindowIcon(QIcon(":app-icon.png"));
    auto* window = new MainWindow();
    window->show();
    return QApplication::exec();
}
