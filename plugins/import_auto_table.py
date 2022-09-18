import importlib
import pathlib
from typing import Optional

from pandas import DataFrame

from src.api import Plugin
from src.api import PluginImport


class ImportPandasLikeTable(PluginImport):
    def __init__(self):
        super().__init__(
            "Таблицу",
            "Загружает таблицу из файла произвольного расширения.",
            supported_formats=['*', '*.csv', '*.xls', '*.xlsx', '*.json', '*.xml']
        )

    def import_from(self, file_path: str, parameters: Plugin.OptionsValues) -> Optional[DataFrame]:
        end = file_path.split('.')[-1]
        if f'read_{end}' in (d := importlib.import_module('pandas').__dict__):
            return d[f'read_{end}'](file_path)
        elif end in ['xls', 'xlsx']:
            return d['read_excel'](file_path)
        else:
            return None


__import_plugins__ = [ImportPandasLikeTable]
__visual_plugins__ = []
