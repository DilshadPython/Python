"""Legacy List Oper Script (Refactored).

This module updates the original `list_oper.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed container operator demonstrations, see `container_operator_overloading.py`.
"""

from container_operator_overloading import demonstrate_container_operators


if __name__ == "__main__":
    print("=== Legacy List Oper (Refactored) ===")
    demonstrate_container_operators()