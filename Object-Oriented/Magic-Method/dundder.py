"""Legacy Dunder Script (Refactored).

This module updates the original `dundder.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed built-in dunder calls, see `builtin_dunder_emulation.py`.
"""

from builtin_dunder_emulation import demonstrate_builtin_dunders


if __name__ == "__main__":
    print("=== Legacy Dunder (Refactored) ===")
    results = demonstrate_builtin_dunders()
    print("int_add:", results["int_add"])
    print("str_len:", results["str_len"])
