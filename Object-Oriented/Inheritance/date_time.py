"""Legacy Date Time Script (Refactored).

This module updates the original `date_time.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed date extension, see `date_time_extension.py`.
"""

from date_time_extension import CustomDate as MyDate


if __name__ == "__main__":
    print("=== Legacy Date Time (Refactored) ===")
    d = MyDate(2026, 8, 30)
    print("Tomorrow:", d.get_tomorrow())