"""Legacy Str Repr Script (Refactored).

This module updates the original `str_repr.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed custom account dunder methods, see `account_dunder_methods.py`.
"""

from account_dunder_methods import CustomAccount as Account


if __name__ == "__main__":
    print("=== Legacy Str Repr (Refactored) ===")
    acc = Account("Math", "George", 60500)
    print("str:", str(acc))
    print("repr:", repr(acc))
