"""Legacy University Script (Refactored).

This module updates the original `university.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed company hierarchy, see `company_hierarchy.py`.
"""

from company_hierarchy import Staff as Student


if __name__ == "__main__":
    print("=== Legacy University (Refactored) ===")
    student = Student("John", "Doe", 0, "Computer Science")
    print("Student Name:", student.get_full_name())
