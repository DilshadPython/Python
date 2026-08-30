"""Legacy Instance Method Script (Refactored).

This module updates the original `instance_method.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed method decorators, see `method_decorators.py`.
"""

from method_decorators import InstanceCounter


if __name__ == "__main__":
    print("=== Legacy Instance Method (Refactored) ===")
    a = InstanceCounter(107)
    print("Instance Value:", a.get_val())
