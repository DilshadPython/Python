"""Legacy Magic Method 1 Script (Refactored).

This module updates the original `magic_method_1.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed custom account dunder methods, see `account_dunder_methods.py`.
"""

from account_dunder_methods import CustomAccount as Account


if __name__ == "__main__":
    print("=== Legacy Magic Method 1 (Refactored) ===")
    acc1 = Account("Math", "George", 60500)
    acc2 = Account("Tom", "Alan", 82500)
    print("Addition (acc1 + acc2):", acc1 + acc2)
    print("len(acc1):", len(acc1))
