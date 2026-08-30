"""Legacy Class Method Script (Refactored).

This module updates the original `class_method.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed class method and factory constructor patterns, see `class_method_factory.py`.
"""

from class_method_factory import Staff


if __name__ == "__main__":
    print("=== Legacy Class Method (Refactored) ===")
    staff1 = Staff("John", "Doe", 4100)
    print("Initial Pay Rate:", Staff.increase_pay_rate)
    Staff.set_increase_pay(1.09)
    print("Updated Pay Rate:", Staff.increase_pay_rate)

    parsed = Staff.from_string("George-Bill-2750")
    print("Parsed Staff:", parsed.full_name(), parsed.salary)