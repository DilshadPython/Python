"""Legacy Split User Script (Refactored).

This module updates the original `split_suer.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed user profile details, see `split_user_details.py`.
"""

from split_user_details import UserProfile as User


if __name__ == "__main__":
    print("=== Legacy Split User (Refactored) ===")
    user = User("John Doe", "19750301")
    print("First Name:", user.first_name)
    print("Last Name:", user.last_name)
    print("Age:", user.calculate_age())
