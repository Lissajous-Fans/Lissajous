#include "core.h"

#include <QApplication>
#include <QDir>
#include <QPluginLoader>

#include "lissapi/interface.h"

namespace Core {
QSet<QString> openable_filetypes = {};

const QSet<QString> &openableFiletypes() {
    return openable_filetypes;
}

static void loadPlugin(QObject *plugin) {
    qDebug() << "Loading plugin: " << plugin;
    auto *import_plugin = qobject_cast<LissAPI::ImportInterface *>(plugin);
    if (import_plugin != nullptr) {
        qInfo() << "Loading import plugin: " << import_plugin;
    }

    auto *view_plugin = qobject_cast<LissAPI::ViewInterface *>(plugin);
    if (view_plugin != nullptr) {
        // ...
    }
}

void loadPlugins() {
    const auto static_instances = QPluginLoader::staticInstances();
    for (auto *plugin : static_instances) {
        loadPlugin(plugin);
    }

    auto plugins_dir = QDir(QApplication::applicationDirPath());
    plugins_dir.cd("plugins");
    for (const auto &plugin_path : plugins_dir.entryList()) {
        QPluginLoader loader(plugins_dir.absoluteFilePath(plugin_path));
        auto *plugin = loader.instance();
        if (plugin != nullptr) {
            loadPlugin(plugin);
        }
    }
}

} // namespace Core
