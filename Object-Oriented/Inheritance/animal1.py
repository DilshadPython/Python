"""Legacy Animal1 Script (Refactored).

This module updates the original `animal1.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed animal hierarchy, see `animal_hierarchy.py`.
"""

from animal_hierarchy import Animal as Animals, Cat, Pigeon as Pigen


if __name__ == "__main__":
    print("=== Legacy Animal1 (Refactored) ===")
    pigeon = Pigen()
    print("Pigeon can fly?:", pigeon.can_fly())
