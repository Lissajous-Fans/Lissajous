import abc

from src.api.plugins import VisualizeType


class ChartAdvice():
    advice_type: VisualizeType
    start_column: int
    end_column: int
    start_row: int
    end_row: int


class BarChartAdvice(ChartAdvice):
    advice_type = VisualizeType.BarChart

    def __init__(self, start_column: int, end_column: int, start_row: int, end_row: int):
        self.start_column = start_column
        self.end_column = end_column
        self.start_row = start_row
        self.end_row = end_row


class LineGraphAdvice(ChartAdvice):
    advice_type = VisualizeType.LineGraph

    def __init__(self, start_column: int, end_column: int, start_row: int, end_row: int):
        self.start_column = start_column
        self.end_column = end_column
        self.start_row = start_row
        self.end_row = end_row


class MapChartAdvice(ChartAdvice):
    advice_type = VisualizeType.Map

    def __init__(self, start_column: int, end_column: int, start_row: int, end_row: int):
        self.start_column = start_column
        self.end_column = end_column
        self.start_row = start_row
        self.end_row = end_row