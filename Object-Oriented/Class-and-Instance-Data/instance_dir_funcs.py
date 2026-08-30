"""Legacy Instance Dir Script (Refactored).

This module updates the original `instance_dir_funcs.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed reflection, see `class_reflection_and_dir.py`.
"""

from class_reflection_and_dir import Person


if __name__ == "__main__":
    print("=== Legacy Instance Dir (Refactored) ===")
    p = Person("Tomas")
    print(dir(p))