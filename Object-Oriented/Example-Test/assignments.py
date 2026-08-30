"""Legacy Assignments Script (Refactored).

This module updates the original `assignments.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed max size list behavior, see `max_size_list.py`.
"""

from max_size_list import MaxSizeList


if __name__ == "__main__":
    print("=== Legacy Assignments (Refactored) ===")
    myobj = MaxSizeList(4)
    myobj.push("Python")
    myobj.push("Java")
    print(myobj.get_list())