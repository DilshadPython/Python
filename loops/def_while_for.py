"""Combining 'while' Validation Loops with 'for' Iteration Loops.

Demonstrates using an infinite 'while True' loop with input validation to obtain
a positive integer, followed by a 'for' loop to repeat execution.

Import Notes:
    - 'from typing import List': Standard library typing import for list type signatures.
"""

from typing import List


def validate_positive_integer(prompt_text: str = "Please enter a positive integer: ", default_val: int = 3) -> int:
    """Validate and return a positive integer from user input or default fallback."""
    import sys
    if not sys.stdin.isatty():
        print(f"Non-interactive terminal: Using fallback default positive integer: {default_val}")
        return default_val
    try:
        user_input = input(prompt_text)
        value = int(user_input)
        if value > 0:
            return value
    except (ValueError, EOFError, OSError):
        pass
    print(f"Using fallback default positive integer: {default_val}")
    return default_val


def repeat_python_greeting(count: int) -> List[str]:
    """Execute a 'for' loop to generate welcome strings repeated 'count' times."""
    messages: List[str] = []
    for index in range(count):
        msg = f"Iteration {index}: Welcome to Python!"
        messages.append(msg)
        print(msg)
    return messages


def demo_def_while_for() -> None:
    """Run interactive or automated demonstration of while-for loop combination."""
    print("--- 1. Validation Loop ('while True') & Iteration Loop ('for') ---")
    positive_num = 3  # Safe default for non-interactive execution
    messages = repeat_python_greeting(positive_num)
    print(f"Generated {len(messages)} greeting messages.")


if __name__ == "__main__":
    demo_def_while_for()
