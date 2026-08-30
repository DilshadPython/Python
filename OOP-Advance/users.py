"""Legacy Users Script (Refactored).

This module updates the original `users.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed staff tracking and namespace introspection, see `staff_management.py`.
"""

from staff_management import Staff


if __name__ == "__main__":
    print("=== Legacy Users (Refactored) ===")
    user = Staff("Tom", "George", 2800)
    print("User Name:", user.full_name())
    print("User Email:", user.email)
    print("User Payment:", user.payment)
    user.increase_payment()
    print("Payment after raise:", user.payment)