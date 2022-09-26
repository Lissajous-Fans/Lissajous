#include "mainwindow.h"

#include <QApplication>
#include <QFileDialog>
#include <QListWidget>
#include <QMenuBar>
#include <QMessageBox>
#include <QPushButton>

#include "core/core.h"

MainWindow::MainWindow() {
    buildMenuBar();
    buildUI();
}

void MainWindow::buildMenuBar() {
    auto *menu_files = menuBar()->addMenu(tr("&File"));
    auto *menu_docks = menuBar()->addMenu(tr("&Docks"));
    auto *menu_help = menuBar()->addMenu(tr("&Help"));

    menu_files->addAction(
        QIcon::fromTheme("document-open"), tr("&Open..."),
        [this] { openFile(QFileDialog::getOpenFileName(this, tr("Choose File"), QDir::homePath())); },
        QKeySequence::Open);
    menu_files->addMenu(QIcon::fromTheme("document-open-recent"), tr("&Recent"));
    menu_files->addAction(QIcon::fromTheme("file-export"), tr("&Export"));
    menu_files->addSeparator();
    menu_files->addAction(QIcon::fromTheme("application-exit"), tr("&Quit"), &QApplication::quit, QKeySequence::Quit);

    menu_docks->addActions({ dock_view_choose->toggleViewAction(), dock_parameters->toggleViewAction() });

    menu_help->addAction(QIcon(":/app-icon.png"), tr("&About Lissajous"), [this] {
        QFile f(":/about/ABOUT.html");
        f.open(QFile::ReadOnly);
        const auto html = f.readAll();
        QMessageBox::about(this, tr("About Lissajous"), html);
        f.close();
    });
    menu_help->addAction(QIcon("text/x-copying"), tr("License"), [this] {
        QFile f(":/about/LICENSE");
        f.open(QFile::ReadOnly);
        QByteArray text = f.readLine();
        while (f.canReadLine()) {
            auto line = f.readLine();
            if (line != "\n")
                text.chop(1);
            else
                text.append('\n');
            text.append(line);
        }
        QMessageBox::about(this, tr("Lissajous License"), text);
        f.close();
    });
    menu_help->addAction(QIcon::fromTheme("qt"), tr("About Qt"), &QApplication::aboutQt);
}

void MainWindow::buildUI() {
    addDockWidget(Qt::LeftDockWidgetArea, dock_view_choose);
    addDockWidget(Qt::RightDockWidgetArea, dock_parameters);

    auto *views_list = new QListWidget(dock_view_choose);
    dock_view_choose->setWidget(views_list);

    for (const auto *view_plugin : Core::viewPlugins()) {
        auto *view_widget = new QListWidgetItem(view_plugin->name(), views_list);
        view_widget->setToolTip(view_plugin->description());
        view_by_list_item[view_widget] = view_plugin;
    }
    connect(views_list, &QListWidget::itemActivated,
        [this](QListWidgetItem *item) { setCentralWidget(view_by_list_item[item]->visualize({})); });
}

void MainWindow::openFile(const QString &path) {
}
