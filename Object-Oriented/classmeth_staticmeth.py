"""Legacy Class/Static Method Script (Refactored).

This module updates the original `classmeth_staticmeth.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed method types and alternative constructors, see `instance_class_static_methods.py`.
"""

import datetime
from instance_class_static_methods import EmployeeService


if __name__ == "__main__":
    print("=== Legacy Class/Static Method (Refactored) ===")
    emp = EmployeeService.from_string("George-Adam-59000")
    print("Parsed Employee Email:", emp.email)
    print("Is 2024-09-13 a workday?:", EmployeeService.is_workday(datetime.date(2024, 9, 13)))