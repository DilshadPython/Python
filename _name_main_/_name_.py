"""Demonstration of Python's built-in `__name__` variable.

When a Python source file is run directly, the Python interpreter sets the
special `__name__` variable to `"__main__"`. When imported by another file,
`__name__` is set to the module's actual file/import name.
"""


def hello() -> str:
    """Return and print the value of `__name__` in the current execution context.

    Returns:
        str: Description string showing the active `__name__` value.
    """
    message = f"The module __name__ in Python is: '{__name__}'"
    print(f"\n{message}")
    return message


# Code inside this block runs ONLY when the script is executed directly.
# It will NOT run if this file is imported as a module by another script.
if __name__ == "__main__":
    hello()
