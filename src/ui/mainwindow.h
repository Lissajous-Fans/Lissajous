#pragma once
#include "lissapi/interface.h"

#include <QDockWidget>
#include <QListWidgetItem>
#include <QMainWindow>
#include <QMenu>
#include <QVBoxLayout>

class MainWindow : public QMainWindow {
public:
    MainWindow();

private:
    QDockWidget *dock_view_choose = new QDockWidget(tr("View"), this);
    QDockWidget *dock_parameters = new QDockWidget(tr("Parameters"), this);
    QMap<QListWidgetItem *, const LissAPI::ViewInterface *> view_by_list_item;

    void buildMenuBar();
    void buildUI();
    void openFile(const QString &path);
};
