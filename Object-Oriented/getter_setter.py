"""Legacy Getter/Setter Script (Refactored).

This module updates the original `getter_setter.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed property getters and setters, see `property_getters_setters.py`.
"""

from property_getters_setters import EmployeeProfile


if __name__ == "__main__":
    print("=== Legacy Getter/Setter (Refactored) ===")
    emp = EmployeeProfile("John", "Doe")
    print("Email Property:", emp.email)
    print("Full Name Property:", emp.full_name)
    emp.full_name = "George Alan"
    print("Updated Full Name:", emp.full_name)
