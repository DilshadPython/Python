"""
Python __name__ Attribute Fundamentals Module.

This module demonstrates:
- How Python sets the special __name__ variable at runtime.
- The difference between direct script execution (__name__ == '__main__')
  and imported module execution (__name__ == 'module_name').
- Inspecting module metadata attributes.
"""

# Import sys for interpreter details
import sys


def get_execution_context() -> dict[str, str]:
    """Retrieve runtime execution context metadata including __name__.

    Returns:
        dict[str, str]: Dictionary containing module name, execution mode, and Python version.
    """
    mode = "Direct Execution (Main Entry Point)" if __name__ == "__main__" else "Imported Module"
    return {
        "module_name": __name__,
        "execution_mode": mode,
        "python_version": sys.version.split()[0],
    }


def format_greeting(caller_name: str = "Developer") -> str:
    """Return a formatted message indicating current execution context.

    Args:
        caller_name (str, optional): Name of caller. Defaults to "Developer".

    Returns:
        str: Formatted string message.
    """
    return f"Hello, {caller_name}! Executing module '{__name__}'."


if __name__ == "__main__":
    context = get_execution_context()
    print("--- Execution Context Metadata ---")
    for key, value in context.items():
        print(f"{key:15s}: {value}")

    print("\n--- Greeting Message ---")
    print(format_greeting())
