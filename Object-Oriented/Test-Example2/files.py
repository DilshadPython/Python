"""Legacy Files Script (Refactored).

This module updates the original `files.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed abstract file writers, see `abstract_file_writers.py`.
"""

from abstract_file_writers import WriteFile, DelimFile, LogFile


if __name__ == "__main__":
    print("=== Legacy Files (Refactored) ===")
    log = LogFile("log_legacy.txt")
    log.write("Legacy log entry")
