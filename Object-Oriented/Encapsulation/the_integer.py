"""Legacy The Integer Script (Refactored).

This module updates the original `the_integer.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed validated integer behavior, see `validated_integer.py`.
"""

from validated_integer import ValidatedInteger


if __name__ == "__main__":
    print("=== Legacy The Integer (Refactored) ===")
    obj = ValidatedInteger()
    obj.set_number(19)
    print("Number:", obj.get_number())
    obj.increment()
    print("Incremented Number:", obj.get_number())
