"""Legacy First Class Script (Refactored).

This module updates the original `first_class.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed pet hierarchy, see `pet_hierarchy.py`.
"""

from pet_hierarchy import Dog


if __name__ == "__main__":
    print("=== Legacy First Class (Refactored) ===")
    mydog = Dog("Raffi", 8, "white", "male")
    print(mydog.description())
