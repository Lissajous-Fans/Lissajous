#pragma once
#include <QSet>
#include <QWidget>

namespace Core {

const QSet<QString> &openableFiletypes();
void loadPlugins();
} // namespace Core
