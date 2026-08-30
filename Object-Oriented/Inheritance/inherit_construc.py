"""Legacy Inherit Constructor Script (Refactored).

This module updates the original `inherit_construc.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed company hierarchy, see `company_hierarchy.py`.
"""

from company_hierarchy import Staff


if __name__ == "__main__":
    print("=== Legacy Inherit Constructor (Refactored) ===")
    s = Staff("Alex", "Jones", 45000, "C++")
    print("Staff Skill:", s.primary_skill)
