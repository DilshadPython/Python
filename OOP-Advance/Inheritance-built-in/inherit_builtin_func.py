"""Legacy Inherit Builtin Func Script (Refactored).

This module updates the original `inherit_builtin_func.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed dictionary subclassing demonstrations, see `dictionary_subclassing.py`.
"""

from dictionary_subclassing import People


if __name__ == "__main__":
    print("=== Legacy Inherit Builtin Func (Refactored) ===")
    obj = People()
    obj["g"] = "Girl"
    obj["b"] = "Boy"
    print("Dict Contents:", dict(obj))
