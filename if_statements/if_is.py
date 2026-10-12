"""Identity ('is') versus Equality ('==') Comparison in Python.

Critical Concept:
- '==' checks VALUE EQUALITY: Do two objects contain the same data?
- 'is' checks OBJECT IDENTITY: Do two variables refer to the EXACT SAME memory location?

Import Notes:
    - 'import sys': Used to query system reference counts and integer/string interning behavior.
    - 'from typing import Dict, Any': Used for structured dictionary type annotations.
"""

import sys
from typing import Dict, Any


def compare_value_and_identity(obj1: Any, obj2: Any) -> Dict[str, Any]:
    """Compare two objects for value equality ('==') and object identity ('is')."""
    return {
        "value_equal": obj1 == obj2,
        "identity_same": obj1 is obj2,
        "id_obj1": id(obj1),
        "id_obj2": id(obj2),
    }


def demo_if_is() -> None:
    """Demonstrate identity vs equality across immutable strings and mutable lists."""
    print("--- 1. Immutable Strings (String Interning) ---")
    student_name = "Tom Smith"
    student = "Tom Smith"
    str_comp = compare_value_and_identity(student_name, student)
    print(f"student_name == student : {str_comp['value_equal']}")
    print(f"student_name is student : {str_comp['identity_same']} (Due to string interning/literals)")
    print(f"id(student_name)        : {str_comp['id_obj1']}")
    print(f"id(student)             : {str_comp['id_obj2']}")

    print("\n--- 2. Mutable Lists (Separate Objects in Memory) ---")
    list_a = ["Python", 3.12, 2026]
    list_b = ["Python", 3.12, 2026]
    list_comp = compare_value_and_identity(list_a, list_b)
    print(f"list_a == list_b        : {list_comp['value_equal']} (Same contents)")
    print(f"list_a is list_b        : {list_comp['identity_same']} (Different objects in heap)")
    print(f"id(list_a)               : {list_comp['id_obj1']}")
    print(f"id(list_b)               : {list_comp['id_obj2']}")

    print("\n--- 3. Variable Aliasing (Shared Object Reference) ---")
    list_c = list_b  # list_c points to the exact same list object as list_b
    alias_comp = compare_value_and_identity(list_b, list_c)
    print(f"list_b == list_c        : {alias_comp['value_equal']}")
    print(f"list_b is list_c        : {alias_comp['identity_same']} (Identical memory reference)")
    print(f"id(list_b) == id(list_c): {alias_comp['id_obj1'] == alias_comp['id_obj2']}")


if __name__ == "__main__":
    print(f"Running on Python runtime {sys.version_info.major}.{sys.version_info.minor}")
    demo_if_is()
