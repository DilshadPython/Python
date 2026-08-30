"""Legacy Second Constructor Script (Refactored).

This module updates the original `second_constructor.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed constructor behavior, see `number_counter.py`.
"""

from number_counter import NumberCounter


if __name__ == "__main__":
    print("=== Legacy Second Constructor (Refactored) ===")
    obj = NumberCounter(3)
    obj.increment()
    obj.increment()
    print("Value:", obj.get_value())