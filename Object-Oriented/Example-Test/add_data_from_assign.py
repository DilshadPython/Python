"""Legacy Max Size List Script (Refactored).

This module updates the original `add_data_from_assign.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed max size list behavior, see `max_size_list.py`.
"""

from max_size_list import MaxSizeList as LanguageList, MaxSizeList


if __name__ == "__main__":
    print("=== Legacy Max Size List (Refactored) ===")
    a_obj = LanguageList(4)
    b_obj = LanguageList(2)

    a_obj.push("Python")
    a_obj.push("Java")
    a_obj.push("C++")
    a_obj.push("JavaScript")

    b_obj.push("A")
    b_obj.push("B")
    b_obj.push("C")

    print("List A:", a_obj.get_list())
    print("List B:", b_obj.get_list())