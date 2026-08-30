"""Legacy Main Script (Refactored).

This module updates the original `main.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed abstract file writers, see `abstract_file_writers.py`.
"""

from abstract_file_writers import LogFile, DelimFile


if __name__ == "__main__":
    print("=== Legacy Main (Refactored) ===")
    log = LogFile("log.txt")
    c = DelimFile("text.csv", ",")

    log.write("Send this message as log")
    c.write(["a", "b", "c", "d"])