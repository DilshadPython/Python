"""Legacy Best Assign Script (Refactored).

This module updates the original `best_assign.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed max size list behavior, see `max_size_list.py`.
"""

from max_size_list import MaxSizeList as LanguageList


if __name__ == "__main__":
    print("=== Legacy Best Assign (Refactored) ===")
    lst = LanguageList(2)
    lst.push("Python")
    lst.push("C++")
    lst.push("Java")
    print(lst.get_list())
