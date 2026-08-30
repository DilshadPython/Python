"""Legacy MRO Script (Refactored).

This module updates the original `mro.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed MRO linearization, see `multiple_inheritance_mro.py`.
"""

from multiple_inheritance_mro import DerivedD1 as D, get_mro_class_names


if __name__ == "__main__":
    print("=== Legacy MRO (Refactored) ===")
    obj = D()
    print("Action:", obj.execute_action())
    print("MRO:", get_mro_class_names(D))
