"""Legacy List Number Addition Script (Refactored).

This module updates the original `add_list_num.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed magic dunder methods, see `magic_dunder_methods.py`.
"""

from magic_dunder_methods import ListNumber


if __name__ == "__main__":
    print("=== Legacy List Number Addition (Refactored) ===")
    flst_1 = ListNumber([1, 2, 3, 4, 5, 6, 3, 4])
    slst_2 = ListNumber([10, 100, 200, 3000, 500, 400, 800, 700])
    total = flst_1 + slst_2
    print("Combined ListNumber:", total)
