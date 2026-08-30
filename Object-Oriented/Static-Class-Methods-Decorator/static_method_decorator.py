"""Legacy Static Method Decorator Script (Refactored).

This module updates the original `static_method_decorator.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed method decorators, see `method_decorators.py`.
"""

from method_decorators import InstanceCounter


if __name__ == "__main__":
    print("=== Legacy Static Method Decorator (Refactored) ===")
    d = InstanceCounter("NonIntegerVal")
    print("Filtered Value:", d.val)
