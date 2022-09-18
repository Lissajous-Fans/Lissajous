import xml.etree.ElementTree
import pandas as pd
import pycountry
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget
from PyQt5.QtSvg import QSvgWidget
from pandas import DataFrame

from src.api import PluginQtVisualize, Plugin, VisualizeType, PluginOptionColor

class MapView(PluginQtVisualize):
    def __init__(self):
        super().__init__("Map View", "No description", VisualizeType.Map)
        self.param_color = PluginOptionColor('Цвет градиента')
        self.parameters.extend([
            self.param_color
        ])
    
    @staticmethod
    def paintCountry(id, color, svg_):
        elm = svg_.find(f'''.//*[@id='{id}']''' )
        elm.attrib['fill'] = f'{color}'
        elm.attrib['style'] = ''

    @staticmethod
    def paintCountriesOneColor(sales, color, svg_):
        mn = float(sales.iat[1, 1])
        mx = float(sales.iat[1, 1])
        for rx in range(1, sales.shape[0]):
            mx = max(mx, float(sales.iat[rx, 1]))
            mn = min(mn, float(sales.iat[rx, 1]))
        raz = mx-mn
        for rx in range(1, sales.shape[0]):
                try:
                    countri = pycountry.countries.get(name = sales.iat[rx, 0])
                    MapView.paintCountry(countri.alpha_2, color.darker(int((float(sales.iat[rx, 1])-mn)/raz*200)).name(), svg_)
                except:
                    pass

    def visualize(self, data: DataFrame, parameters: Plugin.OptionsValues) -> QWidget:
        et = xml.etree.ElementTree.parse('res/world.svg')
        color = parameters[self.param_color]
        MapView.paintCountriesOneColor(data, QColor(255, 0, 0), et)
        et.write('res/snworld.svg')
        svg = QSvgWidget('res/snworld.svg')
        return svg


__import_plugins__ = []
__visual_plugins__ = [MapView]