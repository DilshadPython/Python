"""Legacy Magic Dunder Script (Refactored).

This module updates the original `magic_dunder_class.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed magic dunder methods, see `magic_dunder_methods.py`.
"""

from magic_dunder_methods import EmployeeRecord


if __name__ == "__main__":
    print("=== Legacy Magic Dunder (Refactored) ===")
    emp1 = EmployeeRecord("John", "Doe", "Berlin", 45000)
    emp2 = EmployeeRecord("Tom", "Smith", "Paris", 54000)
    print("str(emp1):", str(emp1))
    print("repr(emp1):", repr(emp1))
    print("emp1 + emp2 combined salary:", emp1 + emp2)