#pragma once

#define QT_STATICPLUGIN

#include <lissapi/interface.h>

#include <QObject>
#include <QtPlugin>

class HelloWorldPlugin : public QObject, public LissAPI::ViewInterface {
    Q_OBJECT;
    Q_PLUGIN_METADATA(IID "org.lissajous-fans.Lissajous.ViewInterface/1.0" FILE "helloworld.json");
    Q_INTERFACES(LissAPI::ViewInterface);

public:
    QWidget *visualize(const LissAPI::Data &data) override;
};
