"""CLI Config File Parser and Manipulation Module.

Usage:
    python3 cli_config_parser.py                     # Reads out full config file
    python3 cli_config_parser.py <key> <value>       # Sets key and value in config file
"""

import sys
from config_dict_file_persistence import ConfigDict


def run_cli() -> None:
    """Execute command-line configuration reading/writing tool."""
    config_file = "config_file.txt"
    config = ConfigDict(config_file)

    if len(sys.argv) == 3:
        key, value = sys.argv[1], sys.argv[2]
        print(f"Writing data to '{config_file}': {key} = {value}")
        config[key] = value
    else:
        print(f"Reading configuration data from '{config_file}':")
        if not config:
            print("  (Configuration file is currently empty)")
        for k, v in config.items():
            print(f"  {k} = {v}")


if __name__ == "__main__":
    run_cli()
