"""Built-in Container Operator Method Demonstration Module.

This module demonstrates built-in container operator behavior and dunder method invocation:
- Concatenation operator (`+`) vs `__add__()` on strings, lists, and tuples.
- Arithmetic subtraction (`-`) vs `__sub__()` on integers.
- Dictionary merging using dictionary unpacking (`**`).
"""

from typing import Dict, List, Tuple


def demonstrate_container_operators() -> None:
    """Demonstrate list, tuple, string, and integer dunder operator methods."""
    print("=== Built-in Container Operator Demonstration ===")

    str1 = "Python"
    str2 = "Language"
    print("String Concatenation (+):", str1 + " " + str2)
    print("String Concatenation (__add__):", str1.__add__(" " + str2))
    print()

    lst1 = ["a", "b", "c"]
    lst2 = ["D", "E", "F"]
    print("List Concatenation (+):", lst1 + lst2)
    print("List Concatenation (__add__):", lst1.__add__(lst2))
    print()

    tp1 = ("A", "B", "C")
    tp2 = ("d", "e", "f")
    print("Tuple Concatenation (+):", tp1 + tp2)
    print("Tuple Concatenation (__add__):", tp1.__add__(tp2))
    print()

    num1, num2 = 232, 137
    print("Integer Addition (+):", num1 + num2)
    print("Integer Addition (__add__):", num1.__add__(num2))
    print("Integer Subtraction (-):", num1 - num2)
    print("Integer Subtraction (__sub__):", num1.__sub__(num2))
    print()

    dict1 = {"a": 11, "b": 22}
    dict2 = {"c": 33, "d": 44}
    merged_dict = {**dict1, **dict2}
    print("Dictionary Merging (Unpacking **):", merged_dict)


if __name__ == "__main__":
    demonstrate_container_operators()
