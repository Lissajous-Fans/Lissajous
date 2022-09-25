#pragma once

#include "data.h"
#include "option.h"
#include <QStringList>
#include <QWidget>


namespace LissAPI {

class ImportInterface {
public:
    virtual ~ImportInterface() = default;

    virtual const QStringList &filetypes() = 0;
    virtual const QVector<Option> &options() = 0;
    virtual Data *import(const QString &path) = 0;
};

class ViewInterface {
public:
    virtual ~ViewInterface() = default;

    virtual QWidget *visualize(const Data &data) = 0;
};
} // namespace LissAPI

Q_DECLARE_INTERFACE(LissAPI::ImportInterface, "org.lissajous-fans.Lissajous.ImportInterface/1.0");
Q_DECLARE_INTERFACE(LissAPI::ViewInterface, "org.lissajous-fans.Lissajous.ViewInterface/1.0");
