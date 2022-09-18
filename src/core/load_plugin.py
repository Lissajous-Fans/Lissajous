from pathlib import Path
from src.api import PluginImport, PluginVisualize, PluginType
from typing import List, Tuple
from importlib import import_module
from PyQt5.QtCore import QStandardPaths


import traceback

def load_all() -> Tuple[List[PluginImport], List[PluginVisualize]]:
    """The first list is list of `PluginImport`s.
    The second is list of `PluginVisualize`s."""
    result = ([], [])
    for plugin_script_path in Path("plugins/").glob("*.py"):
        try:
            for plugin in import_module(
                f"plugins.{plugin_script_path.name.removesuffix('.py')}", "*"
            ).__dict__.get("__plugins__", []):
                if plugin.plugin_type == PluginType.IMPORT:
                    result[0].append(plugin)
                elif plugin.plugin_type == PluginType.VISUALIZE:
                    result[1].append(plugin)
        except Exception as e:
            print(f"Invalid plugin at {plugin_script_path}.")
            traceback.print_exc()
    return result
