#pragma once
#include <QDockWidget>
#include <QMainWindow>
#include <QMenu>

class MainWindow : public QMainWindow {
public:
    MainWindow();

private:
    QDockWidget *dock_view_choose = new QDockWidget(tr("View"), this);
    QDockWidget *dock_parameters = new QDockWidget(tr("Parameters"), this);

    void buildMenuBar();
    void buildUI();
    void openFile(const QString &path);
};
