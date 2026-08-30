"""Legacy Files 2 Script (Refactored).

This module updates the original `files_2.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed formatters, see `file_formatters.py`.
"""

from file_formatters import FileWriter as WriteFile, CSVFormatter, LogFormatter


if __name__ == "__main__":
    print("=== Legacy Files 2 (Refactored) ===")
    write_csv = WriteFile("test2.csv", CSVFormatter)
    write_log = WriteFile("log2.txt", LogFormatter)

    write_csv.write(["a", "b,2", "c", "d"])
    write_log.write("This is a log message")

    write_csv.close()
    write_log.close()