"""Legacy Company Script (Refactored).

This module updates the original `company.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed company hierarchy, see `company_hierarchy.py`.
"""

from company_hierarchy import CompanyEmployee as Company, Staff, Manager


if __name__ == "__main__":
    print("=== Legacy Company (Refactored) ===")
    stf = Staff("Tom", "Henry", 55000, "Python")
    mgr = Manager("Georgina", "Holland", 60000, [stf])
    print("Manager Team:", mgr.get_team_names())