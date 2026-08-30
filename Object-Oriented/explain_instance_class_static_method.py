"""Legacy Method Types Explanation Script (Refactored).

This module updates the original `explain_instance_class_static_method.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed method types and alternative constructors, see `instance_class_static_methods.py`.
"""

import datetime
from instance_class_static_methods import EmployeeService


if __name__ == "__main__":
    print("=== Legacy Method Types Explanation (Refactored) ===")
    emp = EmployeeService("John", "Doe", 47000)
    print("Instance Method:", emp.instance_method()[0])
    print("Static Method Workday Check:", EmployeeService.is_workday(datetime.date(2024, 9, 13)))
