"""Legacy Class Init Script (Refactored).

This module updates the original `class_init.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For comprehensive class initialization details, see `class_definition_init.py`.
"""

from class_definition_init import User


if __name__ == "__main__":
    print("=== Legacy Class Init (Refactored) ===")
    obj_user = User("John", "Doe", 3300)
    print("Full Name:", obj_user.full_name())
    print("Email:", obj_user.email)
    print("Payment:", obj_user.payment)
