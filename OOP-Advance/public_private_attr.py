"""Legacy Public Private Attributes Script (Refactored).

This module updates the original `public_private_attr.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed attribute privacy and encapsulation, see `encapsulation_attributes.py`.
"""

from encapsulation_attributes import Monitor


if __name__ == "__main__":
    print("=== Legacy Public Private Attributes (Refactored) ===")
    obj = Monitor(18)
    print("Protected attribute:", obj._attribute_val)
    print("Mangled attribute:", obj._Monitor__mangled_name)
