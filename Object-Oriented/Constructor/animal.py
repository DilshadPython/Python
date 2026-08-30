"""Legacy Animal Script (Refactored).

This module updates the original `animal.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed animal sound constructor behavior, see `animal_sounds.py`.
"""

from animal_sounds import Animal


if __name__ == "__main__":
    print("=== Legacy Animal (Refactored) ===")
    dogy = Animal("Dog", "barking")
    caty = Animal("Cat", "meowing")
    print(dogy.make_sound())
    print(caty.make_sound())
