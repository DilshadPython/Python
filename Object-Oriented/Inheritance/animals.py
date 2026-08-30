"""Legacy Animals Script (Refactored).

This module updates the original `animals.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed animal hierarchy, see `animal_hierarchy.py`.
"""

from animal_hierarchy import Animal as Animals, Cat, Pigeon as Pigen


if __name__ == "__main__":
    print("=== Legacy Animals (Refactored) ===")
    my_cat = Cat()
    print("Cat can fly?:", my_cat.can_fly())
    print("isinstance(my_cat, Cat):", isinstance(my_cat, Cat))
