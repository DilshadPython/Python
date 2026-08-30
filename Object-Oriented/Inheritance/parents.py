"""Legacy Parents Script (Refactored).

This module updates the original `parents.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed animal hierarchy, see `animal_hierarchy.py`.
"""

from animal_hierarchy import Animal, Cat, Pigeon


if __name__ == "__main__":
    print("=== Legacy Parents (Refactored) ===")
    c = Cat()
    print("Cat fly:", c.can_fly())
