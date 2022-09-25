#include "helloworld.h"

#include <QLabel>

QWidget *HelloWorldPlugin::visualize(const LissAPI::Data & /*data*/) {
    return new QLabel("Hello World!");
}
