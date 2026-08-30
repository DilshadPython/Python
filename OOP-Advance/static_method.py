"""Legacy Static Method Script (Refactored).

This module updates the original `static_method.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed static method utility demonstrations, see `utility_static_method.py`.
"""

import datetime
from utility_static_method import Staff


if __name__ == "__main__":
    print("=== Legacy Static Method (Refactored) ===")
    staff = Staff.from_string("George-Bill-2750")
    print("Staff Name:", staff.full_name())

    monday = datetime.date(2023, 5, 15)
    print("Is Monday a workday?:", Staff.is_workday(monday))