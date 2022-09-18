from typing import Optional

import pandas as pd

from src.api.plugins import PluginImport, Plugin


class ImportCsvTablePlugin(PluginImport):
    def __init__(self):
        super().__init__(
            "Таблица из .csv",
            "Загружает таблицу из формата .csv",
            ['*.csv']
        )

    def import_from(self, file_path: str, parameters: Plugin.OptionsValues) -> Optional[pd.DataFrame]:
        return pd.read_csv(file_path)



__import_plugins__ = [ImportCsvTablePlugin]
__visual_plugins__ = []
