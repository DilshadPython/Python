"""Legacy Basic Class Example Script (Refactored).

This module updates the original `basic_exmp.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For comprehensive class definition basics, see `class_definition_basics.py`.
"""

from class_definition_basics import Employee


if __name__ == "__main__":
    print("=== Legacy Basic Class Example (Refactored) ===")
    first_emp = Employee("John", "Doe", 44)
    second_emp = Employee("Tom", "Smith", 54)

    print(first_emp.get_details())
    print(first_emp.email)
    print("==============================\n")
    print(second_emp.get_details())
    print(second_emp.email)