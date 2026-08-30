"""Legacy Assign2 Script (Refactored).

This module updates the original `assign2.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed formatters, see `file_formatters.py`.
"""

from file_formatters import FileWriter as WriteFile, CSVFormatter, LogFormatter


if __name__ == "__main__":
    print("=== Legacy Assign2 (Refactored) ===")
    csv_writer = WriteFile("test2_legacy.csv", CSVFormatter)
    csv_writer.write(["a", "b,2", "c"])
    csv_writer.close()
