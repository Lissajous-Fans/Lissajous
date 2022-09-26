#pragma once

#include "data.h"
#include "option.h"
#include <QJsonObject>
#include <QStringList>
#include <QWidget>

namespace Core {
    void loadPlugin(QObject *, const QJsonObject&);
} // namespace Core

namespace LissAPI {

class BaseInterface {
public:
    QString name() const { return metadata()["name"].toString(); };
    QString description() const { return metadata()["description"].toString(); };
    const QJsonObject& metadata() const { return _metadata; };

private:
    QJsonObject _metadata;
    friend void Core::loadPlugin(QObject *, const QJsonObject&);
};

class ImportInterface : public BaseInterface {
public:
    virtual ~ImportInterface() = default;

    virtual const QStringList &filetypes() = 0;
    virtual const QVector<Option> &options() = 0;
    virtual Data *import(const QString &path) = 0;
};

class ViewInterface : public BaseInterface {
public:
    virtual ~ViewInterface() = default;

    virtual QWidget *visualize(const Data &data) const = 0;
};

} // namespace LissAPI

Q_DECLARE_INTERFACE(LissAPI::ImportInterface, "org.lissajous-fans.Lissajous.ImportInterface/1.0");
Q_DECLARE_INTERFACE(LissAPI::ViewInterface, "org.lissajous-fans.Lissajous.ViewInterface/1.0");
