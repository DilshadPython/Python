"""Legacy CLI Test Script (Refactored).

This module updates the original `test.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed CLI config parsing, see `cli_config_parser.py`.
"""

from cli_config_parser import run_cli


if __name__ == "__main__":
    run_cli()