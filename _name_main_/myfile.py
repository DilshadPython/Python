"""Helper module illustrating execution context when imported vs run directly.

Notice that functions defined here can be imported by other files (like yourfile.py)
without triggering unwanted top-level code execution if guarded properly.
"""


def hello_py() -> str:
    """Return identification message with current `__name__`.

    Returns:
        str: Message stating module identity and active `__name__`.
    """
    message = (
        f"This file is 'myfile'. Current __name__ is: '{__name__}'\n"
        f"Explanation: When imported, __name__ matches the module name ('myfile'). "
        f"When run directly from terminal, __name__ is '__main__'."
    )
    print(f"\n{message}")
    return message


# If executed directly: python3 myfile.py -> __name__ will be '__main__'
# If imported: `import myfile` from yourfile.py -> this block will NOT execute automatically!
if __name__ == "__main__":
    hello_py()
