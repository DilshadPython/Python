"""Legacy Inherit List Script (Refactored).

This module updates the original `inherit_list.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed 1-based list indexing demonstrations, see `one_based_list.py`.
"""

from one_based_list import MyList


if __name__ == "__main__":
    print("=== Legacy Inherit List (Refactored) ===")
    obj = MyList(["ABc", "DEf", "GEh", "IJk"])
    print("MyList Index 1:", obj[1])
    print("MyList Index 4:", obj[4])
