from pathlib import Path
from src.api import PluginImport, PluginVisualize
from typing import List, Tuple
from importlib import import_module
from PyQt5.QtCore import QStandardPaths


def load_all() -> Tuple[List[PluginImport], List[PluginVisualize]]:
    """The first list is list of `PluginImport`s.
    The second is list of `PluginVisualize`s."""
    result = ([], [])
    for plugin_script_path in Path("plugins/").glob("*.py"):
        try:
            for plugin in import_module(
                f"..{plugin_script_path.name.removesuffix('py')}"
            ).__dict__.get("__plugins__", []):
                if isinstance(plugin, PluginImport):
                    result[0].append(plugin)
                elif isinstance(plugin, PluginVisualize):
                    result[1].append(plugin)
        except Exception:
            print(f"Invalid plugin at {plugin_script_path}")
    return result
