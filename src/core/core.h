#pragma once

#include "lissapi/interface.h"

#include <QMap>
#include <QWidget>

namespace Core {

const QMap<QString, QVector<LissAPI::ImportInterface *>>& openableFiletypes();
const QVector<LissAPI::ViewInterface *>& viewPlugins();
void loadPlugins();
} // namespace Core
