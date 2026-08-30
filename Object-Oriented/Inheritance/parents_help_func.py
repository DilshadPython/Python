"""Legacy Parents Help Function Script (Refactored).

This module updates the original `parents_help_func.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed company hierarchy, see `company_hierarchy.py`.
"""

from company_hierarchy import Manager


if __name__ == "__main__":
    print("=== Legacy Parents Help Function (Refactored) ===")
    mgr = Manager("Georgina", "Holland", 12000)
    print("Manager Full Name:", mgr.get_full_name())
