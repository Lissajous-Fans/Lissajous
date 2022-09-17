from src.api.plugins import VisualizeType


class ChartAdvice:
    advice_type: VisualizeType = VisualizeType.Undefined
    start_column: int
    end_column: int
    start_row: int
    end_row: int

    def __init__(self, start_column: int, end_column: int, start_row: int, end_row: int):
        self.start_column = start_column
        self.end_column = end_column
        self.start_row = start_row
        self.end_row = end_row

    def __repr__(self) -> str:
        return f"ChartAdvice({self.advice_type}, {self.start_column}, {self.end_column}, {self.start_row}, {self.end_row})"


class BarChartAdvice(ChartAdvice):
    advice_type = VisualizeType.BarChart


class LineGraphAdvice(ChartAdvice):
    advice_type = VisualizeType.LineGraph


class MapChartAdvice(ChartAdvice):
    advice_type = VisualizeType.Map
