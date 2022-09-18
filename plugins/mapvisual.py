from xml.etree import ElementTree
from xml.etree.ElementTree import ElementTree as XMLTree

import pycountry
from lissapi import (
    Plugin,
    PluginOptionColor,
    PluginVisualize,
    VisualizeType,
    PluginOption,
)
from pandas import DataFrame
from typing import Tuple
from PyQt5.QtGui import QColor
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTemporaryFile, Qt


class MapView(PluginVisualize):
    def __init__(self):
        super().__init__("Map View", "No description", VisualizeType.Map, ["*.svg"])
        self.param_color = PluginOptionColor("Gradient Color")
        # self.parameters.extend([self.param_color])

    @staticmethod
    def fill_country(id, color, svg):
        elm = svg.find(f".//*[@id='{id}']")
        elm.attrib["fill"] = f"{color}"

    @staticmethod
    def paint_countries_one_color(sales, color, svg):
        mn = float(sales.iat[1, 1])
        mx = float(sales.iat[1, 1])
        for rx in range(1, sales.shape[0]):
            mx = max(mx, float(sales.iat[rx, 1]))
            mn = min(mn, float(sales.iat[rx, 1]))
        raz = mx - mn
        for rx in range(1, sales.shape[0]):
            try:
                country = pycountry.countries.get(name=sales.iat[rx, 0])
                MapView.fill_country(
                    country.alpha_2,
                    color.darker(
                        int((float(sales.iat[rx, 1]) - mn) / raz * 200)
                    ).name(),
                    svg,
                )
            except:
                pass

    def visualize(
        self, data: DataFrame, parameters: Plugin.OptionsValues
    ) -> Tuple[QWidget, XMLTree]:
        et = ElementTree.parse("res/world.svg")
        color = QColor(200, 0, 100) # parameters[self.param_color]
        MapView.paint_countries_one_color(data, QColor(255, 0, 0), et)
        temp_file = QTemporaryFile()
        temp_file.open()
        path = temp_file.fileName()
        et.write(path)
        svg = QSvgWidget(path)
        svg.renderer().setAspectRatioMode(Qt.KeepAspectRatio)
        return (svg, et)

    def export_to(
        self,
        file_path: str,
        data: DataFrame,
        svg_tree: XMLTree,
        parameters: PluginOption,
    ) -> bool:
        svg_tree.write(file_path)
        return True


__plugins__ = [MapView()]
__import_plugins__ = []
__visual_plugins__ = [MapView]
