"""Demonstration of calling a function guarded by `__name__ == '__main__'`.

This pattern allows scripts to define reusable functions that can be imported
elsewhere while also providing an executable entry point when run directly.
"""


def callme() -> str:
    """Print and return the execution context of the module.

    Returns:
        str: Description string showing current module name.
    """
    message = f"The module __name__ in Python is: '{__name__}'"
    print(f"\n{message}")
    return message


if __name__ == "__main__":
    callme()
