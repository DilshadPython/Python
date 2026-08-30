"""Legacy Magic Method Script (Refactored).

This module updates the original `magic_method.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed custom account dunder methods, see `account_dunder_methods.py`.
"""

from account_dunder_methods import CustomAccount as Account


if __name__ == "__main__":
    print("=== Legacy Magic Method (Refactored) ===")
    account_1 = Account("Math", "George", 60500)
    print("str(account_1):", str(account_1))
    print("repr(account_1):", repr(account_1))
