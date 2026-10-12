"""
Python Easter Egg: `import __hello__` (Frozen Module Hello World)

`__hello__` is a built-in frozen CPython module created to test CPython's
frozen import mechanism (`PyImport_ImportFrozenModule`).

When imported, it immediately prints "Hello world!".
In Python 3.11+, additional test packages like `__phello__` and `__phello__.spam`
were introduced for testing frozen packages.

Example:
    >>> import __hello__
    Hello world!
"""
import io
import sys
import contextlib
import __hello__


def capture_hello_output() -> str:
    """
    Imports and executes `__hello__.main()` (or captures top-level module output)
    redirecting stdout to capture its printed output.

    Returns:
        str: The string printed by the `__hello__` frozen module ("Hello world!").
    """
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        if hasattr(__hello__, "main"):
            __hello__.main()
        else:
            import importlib
            importlib.reload(__hello__)
    return buffer.getvalue().strip()


def capture_phello_output() -> str:
    """
    Imports `__phello__.spam` (Python 3.11+) if available to demonstrate frozen package imports.

    Returns:
        str: Output captured from `__phello__.spam`, or fallback message if unavailable.
    """
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            import __phello__.spam  # noqa: F401
        return buffer.getvalue().strip()
    except (ImportError, AttributeError):
        return "Frozen package `__phello__.spam` unavailable in this Python version"


def main() -> None:
    """Executes the `__hello__` frozen module demonstration."""
    print("=" * 60)
    print("👋 Python Easter Egg: Frozen Hello World (`import __hello__`)")
    print("=" * 60)

    output = capture_hello_output()
    print(f"\nCaptured output from `import __hello__`: {output!r}")

    phello_output = capture_phello_output()
    print(f"Captured output from `import __phello__.spam`: {phello_output!r}")

    print("\nExplanation:")
    print("  `__hello__` is a minimal CPython frozen module binary compiled into the runtime.")
    print("  It serves as an automated test fixture for CPython's frozen module loader.")


if __name__ == "__main__":
    main()
