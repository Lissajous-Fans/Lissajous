#include "core/core.h"
#include "ui/mainwindow.h"

#include <QApplication>
#include <QtPlugin>

Q_IMPORT_PLUGIN(HelloWorldPlugin)

int main(int argc, char **args) {
    new QApplication(argc, args);
    QApplication::setApplicationName("Lissajous");
    QApplication::setOrganizationName("Lissajous-Fans");
    QApplication::setWindowIcon(QIcon(":app-icon.png"));
    Core::loadPlugins();
    auto *window = new MainWindow();
    window->show();
    return QApplication::exec();
}
