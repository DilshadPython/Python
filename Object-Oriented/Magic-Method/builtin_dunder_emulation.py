"""Built-in Dunder Method Emulation Module.

This module demonstrates how built-in operators (+, -, *, len) translate directly into underlying dunder method calls
such as `__add__`, `__sub__`, `__mul__`, and `__len__`.
"""


def demonstrate_builtin_dunders() -> dict:
    """Execute direct built-in dunder method calls and return results dictionary.

    Returns:
        Dictionary of operation results.
    """
    return {
        "int_add": int.__add__(33, 17),
        "float_add": float.__add__(21.098, 87.83),
        "str_add": str.__add__("A", "B"),
        "float_sub": float.__sub__(87.83, 21.098),
        "float_mul": float.__mul__(2.5, 4.0),
        "str_len": "Hello world".__len__(),
    }


if __name__ == "__main__":
    print("=== Built-in Dunder Emulation Demonstration ===")
    results = demonstrate_builtin_dunders()
    for key, val in results.items():
        print(f"  {key}: {val}")
