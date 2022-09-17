from lissapi import *


class LineGraphView(VisualizePlugin):
    def __init__(self):
        super().__init__("Line Graph View", "Line Graph View.", VisualizeType.LineGraph)
