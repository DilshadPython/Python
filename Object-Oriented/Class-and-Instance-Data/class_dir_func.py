"""Legacy Class Dir Script (Refactored).

This module updates the original `class_dir_func.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed reflection, see `class_reflection_and_dir.py`.
"""

from class_reflection_and_dir import Person, inspect_all_dunder_attributes


if __name__ == "__main__":
    print("=== Legacy Class Dir (Refactored) ===")
    p = Person("Tomas")
    print("Dir:", dir(Person))
    print("Dunders:", inspect_all_dunder_attributes(p))
