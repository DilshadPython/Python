"""Legacy Log Script (Refactored).

This module updates the original `log.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed formatters, see `file_formatters.py`.
"""

import datetime


if __name__ == "__main__":
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print("Formatted Date:", date_str)