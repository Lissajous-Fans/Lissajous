from typing import Optional

import pandas as pd

from src.api.plugins import PluginImport, Plugin


class ImportFromExcelFile(PluginImport):
    def __init__(self):
        super().__init__(
            "Таблица из .xlsx",
            "Загружает таблицу из формата .excel",
            ['*.xlsx']
        )

    def import_from(self, file_path: str, parameters: Plugin.OptionsValues) -> Optional[pd.DataFrame]:
        return pd.read_excel(file_path, index_col=None, header=None)


__import_plugins__ = [ImportFromExcelFile]
__visual_plugins__ = []
