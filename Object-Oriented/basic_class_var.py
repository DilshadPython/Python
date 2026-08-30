"""Legacy Class Variable Script (Refactored).

This module updates the original `basic_class_var.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed class and instance attributes, see `class_and_instance_attributes.py`.
"""

from class_and_instance_attributes import EmployeeAccount


if __name__ == "__main__":
    print("=== Legacy Basic Class Variable (Refactored) ===")
    emp1 = EmployeeAccount("John", "Doe", 47000)
    emp2 = EmployeeAccount("Tom", "Smith", 55000)

    print("Total Employees:", EmployeeAccount.total_employee_count)
    print("emp1 salary before raise:", emp1.salary)
    emp1.apply_pay_raise()
    print("emp1 salary after default raise:", emp1.salary)
