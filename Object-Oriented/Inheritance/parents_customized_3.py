"""Legacy Parents Customized 3 Script (Refactored).

This module updates the original `parents_customized_3.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed company hierarchy, see `company_hierarchy.py`.
"""

from company_hierarchy import Staff, Manager


if __name__ == "__main__":
    print("=== Legacy Parents Customized 3 (Refactored) ===")
    stf = Staff("Joe", "Philips", 7000, "Java")
    mgr = Manager("Georgina", "Holland", 12000, [stf])
    print("Team:", mgr.get_team_names())
