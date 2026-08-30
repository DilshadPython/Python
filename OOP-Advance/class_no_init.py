"""Legacy Class Without Init Script (Refactored).

This module updates the original `class_no_init.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed dynamic attribute assignment without init, see `class_attributes_no_init.py`.
"""

from class_attributes_no_init import DynamicUser as User


if __name__ == "__main__":
    print("=== Legacy Class Without Init (Refactored) ===")
    user = User()
    user.first_name = "Alex"
    user.last_name = "Morgan"
    print("User:", user.first_name, user.last_name)
