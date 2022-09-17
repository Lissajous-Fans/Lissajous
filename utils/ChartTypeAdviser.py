import pandas as pd

import src.utils.ChartAdvices as advices
from src.utils.ChartAdvices import ChartAdvice


class ChartTypeAdviser:
    def __search_for_linear_chart(self, table: pd.DataFrame) -> advices.LineGraphAdvice:
        is_int = [[False for i in range(len(table))] for j in range(len(table.columns))]
        for i in range(len(table.columns)):
            for j in range(len(table)):
                is_int[i][j] = (isinstance(table[i][j], int) or isinstance(table[i][j], float)) and pd.notna(
                    table[i][j])
        dp_horizontal = [[1 if is_int[i][j] else 0 for j in range(len(table))] for i in range(len(table.columns))]
        dp_vertical = [[1 if is_int[i][j] else 0 for j in range(len(table))] for i in range(len(table.columns))]
        for i in range(len(table.columns)):
            for j in range(len(table)):
                if i != 0:
                    dp_horizontal[i][j] = dp_horizontal[i - 1][j] + 1
                    if not (is_int[i][j]):
                        dp_horizontal[i][j] = 0

                if j != 0:
                    dp_vertical[i][j] = dp_vertical[i][j - 1] + 1
                    if not (is_int[i][j]):
                        dp_vertical[i][j] = 0

        mxln = -1
        mx_i = -1
        mx_j = -1
        for i in range(1, len(table.columns)):
            for j in range(len(table)):
                if dp_horizontal[i][j] >= 2:
                    new_ln = min(dp_vertical[i][j], dp_vertical[i - 1][j])
                    if new_ln > mxln:
                        mxln = new_ln
                        mx_i = i
                        mx_j = j

        if mxln > 3:
            return advices.LineGraphAdvice(mx_i - 1, mx_i, mx_j - mxln + 1, mx_j)
        else:
            return None

    def __search_for_bar_chart(self, table: pd.DataFrame) -> advices.BarChartAdvice:
        is_int = [[False for i in range(len(table))] for j in range(len(table.columns))]
        is_str = [[False for i in range(len(table))] for j in range(len(table.columns))]
        for i in range(len(table.columns)):
            for j in range(len(table)):
                is_int[i][j] = (isinstance(table[i][j], int) or isinstance(table[i][j], float)) and pd.notna(
                    table[i][j])
                is_str[i][j] = isinstance(table[i][j], str)
        dp_horizontal = [[1 if is_int[i][j] else 0 for j in range(len(table))] for i in range(len(table.columns))]
        dp_vertical = [[1 if is_int[i][j] else 0 for j in range(len(table))] for i in range(len(table.columns))]

        dp_horizontal_str = [[1 if is_str[i][j] else 0 for j in range(len(table))] for i in range(len(table.columns))]
        dp_vertical_str = [[1 if is_str[i][j] else 0 for j in range(len(table))] for i in range(len(table.columns))]
        for i in range(len(table.columns)):
            for j in range(len(table)):
                if i != 0:
                    dp_horizontal[i][j] = dp_horizontal[i - 1][j] + 1
                    if not (is_int[i][j]):
                        dp_horizontal[i][j] = 0

                    dp_horizontal_str[i][j] = dp_horizontal_str[i - 1][j] + 1
                    if not (is_str[i][j]):
                        dp_horizontal_str[i][j] = 0

                if j != 0:
                    dp_vertical[i][j] = dp_vertical[i][j - 1] + 1
                    if not (is_int[i][j]):
                        dp_vertical[i][j] = 0

                    dp_vertical_str[i][j] = dp_vertical_str[i][j - 1] + 1
                    if not (is_str[i][j]):
                        dp_vertical_str[i][j] = 0

        mxln = -1
        mx_i = -1
        mx_s = 0
        mx_j = -1
        for i in range(1, len(table.columns)):
            for j in range(len(table)):
                for k in range(2, 5):
                    if i - k < 0:
                        continue
                    new_len = 10 ** 9
                    for s in range(k):
                        new_len = min(new_len, dp_vertical_str[i - k][j], dp_vertical[max(0, i - s)][j])
                    if new_len > mxln:
                        mxln = new_len
                        mx_s = k
                        mx_i = i
                        mx_j = j

        if mxln > 3:
            return advices.BarChartAdvice(mx_i - (mx_s - 1) - 1, mx_i, mx_j - mxln + 1, mx_j)
        else:
            return None

    def get_advices(self, table:pd.DataFrame) -> [ChartAdvice]:
        result = []
        i = self.__search_for_linear_chart(table)
        if i is not None:
            result.append(i)
        i = self.__search_for_bar_chart(table)
        if i is not None:
            result.append(i)
        return result
