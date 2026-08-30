"""Legacy Regular Method Script (Refactored).

This module updates the original `regular_method.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed instance method demonstrations, see `instance_regular_method.py`.
"""

from instance_regular_method import Staff


if __name__ == "__main__":
    print("=== Legacy Regular Method (Refactored) ===")
    staff1 = Staff("John", "Doe", 4100)
    print("Full Name:", staff1.full_name())
    print("Email:", staff1.show_email())
    print("Salary:", staff1.salary)
    staff1.increase_salary()
    print("Updated Salary:", staff1.salary)