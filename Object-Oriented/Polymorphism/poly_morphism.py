"""Legacy Polymorphism Script (Refactored).

This module updates the original `poly_morphism.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed polymorphism behavior, see `polymorphic_animals.py`.
"""

from polymorphic_animals import Animal, Dog, Cat, express_all_affections


if __name__ == "__main__":
    print("=== Legacy Polymorphism (Refactored) ===")
    pets = [Dog("Raffi"), Cat("Smikey"), Cat("Ali"), Dog("Tilly")]
    for msg in express_all_affections(pets):
        print(msg)
