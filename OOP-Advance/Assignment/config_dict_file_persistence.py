"""Persistent Configuration Dictionary Module.

This module implements `ConfigDict`, a specialized dictionary subclass that loads
key-value pairs from a text configuration file on initialization and automatically
syncs key-value updates back to disk on item assignment (`__setitem__`).
"""

import os
from typing import Any, Dict


class ConfigDict(dict):
    """Dictionary subclass providing automatic text file persistence for key-value configuration."""

    def __init__(self, filename: str) -> None:
        """Initialize ConfigDict, loading existing key-value pairs if the file exists.

        Args:
            filename: Path to the configuration text file.
        """
        super().__init__()
        self._filename: str = filename

        if os.path.isfile(self._filename):
            with open(self._filename, "r", encoding="utf-8") as file_handle:
                for line in file_handle:
                    stripped_line = line.strip()
                    if stripped_line and "=" in stripped_line:
                        key, value = stripped_line.split("=", 1)
                        dict.__setitem__(self, key.strip(), value.strip())

    def __setitem__(self, key: Any, value: Any) -> None:
        """Assign key-value pair and rewrite persistent configuration file.

        Args:
            key: Configuration key.
            value: Configuration value.
        """
        dict.__setitem__(self, key, value)
        with open(self._filename, "w", encoding="utf-8") as file_handle:
            for k, v in self.items():
                file_handle.write(f"{k}={v}\n")


if __name__ == "__main__":
    print("=== Persistent Configuration Dictionary Demonstration ===")
    config_file_path = "config.txt"
    config = ConfigDict(config_file_path)

    config["host"] = "localhost"
    config["port"] = "8080"
    config["mode"] = "debug"

    print("Config Dict Contents in Memory:", dict(config))
    print(f"Verified configuration written to disk in '{config_file_path}'")
