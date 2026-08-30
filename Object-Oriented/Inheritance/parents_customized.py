"""Legacy Parents Customized Script (Refactored).

This module updates the original `parents_customized.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed company hierarchy, see `company_hierarchy.py`.
"""

from company_hierarchy import Staff, Manager


if __name__ == "__main__":
    print("=== Legacy Parents Customized (Refactored) ===")
    stf = Staff("Joe", "Philips", 7000, "Java")
    print("Staff Skill:", stf.primary_skill)
