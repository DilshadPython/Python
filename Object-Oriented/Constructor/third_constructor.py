"""Legacy Third Constructor Script (Refactored).

This module updates the original `third_constructor.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed constructor behavior, see `number_counter.py`.
"""

from number_counter import NumberCounter


if __name__ == "__main__":
    print("=== Legacy Third Constructor (Refactored) ===")
    obj = NumberCounter(3)
    obj.increment()
    obj.increment()
    print("Value:", obj.get_value())

    obj_str = NumberCounter("Welcome")
    print("String Input Value:", obj_str.get_value())
