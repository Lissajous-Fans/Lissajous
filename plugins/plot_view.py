import io
from io import BytesIO

from matplotlib import pyplot as plt
from pandas import DataFrame

from api.plugins import Plugin, PluginOptionColor
from src.api.plugins import PluginVisualize, VisualizeType, PluginOptionString


class PlotViewPlugin(PluginVisualize):
    def __init__(self):
        super().__init__(
            "Plot View",
            "Draw plot.",
            VisualizeType.LineGraph,
        )
        self.option_x = PluginOptionString('X')
        self.option_y = PluginOptionString('Y')
        self.option_line_color = PluginOptionColor('Цвет графика')
        self.parameters.extend([
            self.option_x,
            self.option_y,
            self.option_line_color
        ])

    def visualize(self, data: DataFrame, parameters: Plugin.OptionsValues) -> BytesIO:
        print(parameters)
        plt.plot(
            parameters[self.option_x],
            parameters[self.option_y],
            parameters[self.option_line_color]
        )
        buffer = io.BytesIO()
        plt.savefig(buffer, format='PNG')
        return buffer


__visual_plugins__ = [PlotViewPlugin]
__import_plugins__ = []
