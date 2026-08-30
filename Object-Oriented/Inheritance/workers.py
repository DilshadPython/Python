"""Legacy Workers Script (Refactored).

This module updates the original `workers.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed company hierarchy, see `company_hierarchy.py`.
"""

from company_hierarchy import CompanyEmployee as Worker


if __name__ == "__main__":
    print("=== Legacy Workers (Refactored) ===")
    worker = Worker("Alice", "Smith", 45000)
    print("Worker Full Name:", worker.get_full_name())