"""Legacy Company Script (Refactored).

This module updates the original `company.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed user accounts, see `user_account.py`.
"""

from user_account import UserAccount as Employee


if __name__ == "__main__":
    print("=== Legacy Company (Refactored) ===")
    emp = Employee("Jane", "Doe")
    print("Employee:", emp.get_full_name())
