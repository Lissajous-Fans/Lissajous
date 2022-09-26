#include "core.h"

#include <QApplication>
#include <QDir>
#include <QMap>
#include <QPluginLoader>

#include "lissapi/interface.h"

namespace Core {
QMap<QString, QVector<LissAPI::ImportInterface *>> openable_filetypes = {};
QVector<LissAPI::ViewInterface *> view_plugins = {};

const QMap<QString, QVector<LissAPI::ImportInterface *>>& openableFiletypes() {
    return openable_filetypes;
}

const QVector<LissAPI::ViewInterface *>& viewPlugins() {
    return view_plugins;
}

void loadPlugin(QObject *plugin, const QJsonObject& metadata) {
    qDebug() << "Loading plugin: " << plugin;
    auto *base_plugin = dynamic_cast<LissAPI::BaseInterface *>(plugin);
    base_plugin->_metadata = metadata["MetaData"].toObject();

    auto *import_plugin = qobject_cast<LissAPI::ImportInterface *>(plugin);
    if (import_plugin != nullptr) {
        for (const auto filetypes = import_plugin->filetypes(); const auto &ft : filetypes) {
            if (!openable_filetypes.contains(ft))
                openable_filetypes[ft] = QVector<LissAPI::ImportInterface *> { import_plugin };
            else
                openable_filetypes[ft].push_back(import_plugin);
        }
    }

    auto *view_plugin = qobject_cast<LissAPI::ViewInterface *>(plugin);
    if (view_plugin != nullptr) {
        qDebug() << "Is View Plugin";
        view_plugins.append(view_plugin);
    }
}

void loadPlugins() {
    for (const auto static_plugins = QPluginLoader::staticPlugins(); const auto& plugin : static_plugins) {
        loadPlugin(plugin.instance(), plugin.metaData());
    }

    auto plugins_dir = QDir(QApplication::applicationDirPath());
    plugins_dir.cd("plugins");
    for (const auto &plugin_path : plugins_dir.entryList()) {
        QPluginLoader loader(plugins_dir.absoluteFilePath(plugin_path));
        auto *plugin = loader.instance();
        if (plugin != nullptr) {
            loadPlugin(plugin, loader.metaData());
        }
    }
}

} // namespace Core
