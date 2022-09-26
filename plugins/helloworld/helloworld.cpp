#include "helloworld.h"

#include <QLabel>

QWidget *HelloWorldPlugin::visualize(const LissAPI::Data & /*data*/) const {
    return new QLabel("Hello World!");
}
