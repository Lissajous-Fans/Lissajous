#pragma once
#include <QMainWindow>
#include <QMenu>

class MainWindow : public QMainWindow {
public:
    MainWindow();

private:
    void buildMenuBar();
    void openFile(const QString& path);
};
