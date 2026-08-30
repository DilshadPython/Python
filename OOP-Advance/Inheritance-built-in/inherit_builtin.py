"""Legacy Inherit Builtin Script (Refactored).

This module updates the original `inherit_builtin.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed dictionary subclassing demonstrations, see `dictionary_subclassing.py`.
"""

from dictionary_subclassing import People


if __name__ == "__main__":
    print("=== Legacy Inherit Builtin (Refactored) ===")
    obj = People()
    obj["f"] = "Female"
    obj["m"] = "Male"
    print("Dict Contents:", dict(obj))
