"""Legacy Account Script (Refactored).

This module updates the original `account.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed user accounts, see `user_account.py`.
"""

from user_account import UserAccount as User


if __name__ == "__main__":
    print("=== Legacy Account (Refactored) ===")
    user_1 = User("John", "Doe")
    user_2 = User("Daniel", "Edward")
    print(user_1.get_full_name())
    print(user_2.get_full_name())
