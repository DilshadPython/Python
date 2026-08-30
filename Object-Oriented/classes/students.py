"""Legacy Students Script (Refactored).

This module updates the original `students.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed user accounts, see `user_account.py`.
"""

from user_account import UserAccount as Student


if __name__ == "__main__":
    print("=== Legacy Students (Refactored) ===")
    s = Student("Alice", "Smith")
    print("Student Name:", s.get_full_name())
