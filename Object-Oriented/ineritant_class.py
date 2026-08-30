"""Legacy Inheritance Script (Refactored).

This module updates the original `ineritant_class.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed class inheritance and MRO, see `class_inheritance_and_mro.py`.
"""

from class_inheritance_and_mro import Employee, Developer, Manager


if __name__ == "__main__":
    print("=== Legacy Inheritance (Refactored) ===")
    dev = Developer("John", "Doe", "Berlin", 45000, "Python")
    mgr = Manager("Elmot", "David", "Cologne", 85300, [dev])
    print("Developer Email:", dev.email)
    print("Manager Team:", mgr.list_team_members())
    print("isinstance(dev, Employee):", isinstance(dev, Employee))