#include "mainwindow.h"

#include <QApplication>
#include <QFileDialog>
#include <QMenu>
#include <QMenuBar>
#include <QMessageBox>

MainWindow::MainWindow() {
    buildMenuBar();
}

void MainWindow::buildMenuBar() {
    auto* menu_files = menuBar()->addMenu(tr("&File"));
    auto* menu_help = menuBar()->addMenu(tr("&Help"));

    auto* action_open = menu_files->addAction(QIcon::fromTheme("document-open"), tr("&Open..."));
    auto* menu_recent = menu_files->addMenu(QIcon::fromTheme("document-open-recent"), tr("&Recent"));
    auto* action_export = menu_files->addAction(QIcon::fromTheme("file-export"), tr("&Export"));
    menu_files->addSeparator();
    auto* action_quit = menu_files->addAction(QIcon::fromTheme("application-exit"), tr("&Quit"));

    auto* action_about = menu_help->addAction(QIcon(":/app-icon.png"), tr("&About Lissajous"));
    auto* action_license = menu_help->addAction(QIcon("text-x-copying"), tr("License"));
    auto* action_about_qt = menu_help->addAction(QIcon::fromTheme("qt"), tr("About Qt"));

    action_open->setShortcut(QKeySequence::Open);
    action_quit->setShortcut(QKeySequence::Quit);

    connect(action_open, &QAction::triggered,
        [this] { openFile(QFileDialog::getOpenFileName(this, tr("Choose File"), QDir::homePath())); });
    connect(action_quit, &QAction::triggered, qApp, &QApplication::quit, Qt::QueuedConnection);

    connect(action_about, &QAction::triggered, [this] {
        QFile f(":/about/ABOUT.html");
        f.open(QFile::ReadOnly);
        auto html = f.readAll();
        QMessageBox::about(this, tr("About Lissajous"), html);
        f.close();
    });
    connect(action_license, &QAction::triggered, [this] {
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
        QMessageBox::about(this, tr("RayMarcher License"), text);
        f.close();
    });
    connect(action_about_qt, &QAction::triggered, &QApplication::aboutQt);
}

void MainWindow::openFile(const QString& path) {
}
