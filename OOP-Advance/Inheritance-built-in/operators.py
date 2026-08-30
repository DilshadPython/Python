"""Legacy Operators Script (Refactored).

This module updates the original `operators.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed container operator demonstrations, see `container_operator_overloading.py`.
"""

from container_operator_overloading import demonstrate_container_operators


if __name__ == "__main__":
    print("=== Legacy Operators (Refactored) ===")
    demonstrate_container_operators()
