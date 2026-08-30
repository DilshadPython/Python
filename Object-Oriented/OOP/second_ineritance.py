"""Legacy Second Inheritance Script (Refactored).

This module updates the original `second_ineritance.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed pet hierarchy, see `pet_hierarchy.py`.
"""

from pet_hierarchy import Dog, Cat


if __name__ == "__main__":
    print("=== Legacy Second Inheritance (Refactored) ===")
    mydog = Dog("Raffi", 8, "white", "male")
    mycat = Cat("Mimi", 2, "black", "female")
    print("Dog Sound:", mydog.speak())
    print("Cat Sound:", mycat.speak())
