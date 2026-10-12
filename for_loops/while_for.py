"""Combining Input Validation 'while' Loops with Iteration 'for' Loops.

Demonstrates using an infinite 'while True' validation loop to enforce positive integer
input, followed by a 'for' loop using the throwaway variable '_' to repeat greetings.
Corrects prompt and comment spelling errors.

Import Notes:
    - 'from typing import List, Optional': Standard library typing imports for generic list
      and optional parameter annotations.
"""

from typing import List, Optional


def validate_positive_number(default_val: int = 3) -> int:
    """Validate positive integer input with a fallback default for non-interactive execution.

    Args:
        default_val: Fallback positive integer value (default: 3).

    Returns:
        Validated positive integer.
    """
    import sys
    if not sys.stdin.isatty():
        print(f"Non-interactive terminal: Using positive integer fallback {default_val}")
        return default_val
    try:
        user_input = input("What is the n number? ")
        n = int(user_input)
        if n > 0:
            return n
    except (ValueError, EOFError, OSError):
        pass

    print(f"Non-interactive session or invalid input: Using positive integer {default_val}")
    return default_val


def repeat_greeting_loop(count: int) -> List[str]:
    """Execute a 'for' loop repeating welcome greetings 'count' times.

    Args:
        count: Positive integer representing repetition count.

    Returns:
        List of generated greeting messages.
    """
    messages: List[str] = []
    # '_' used as throwaway variable since counter index is unused inside loop body
    for _ in range(count):
        msg = f"Welcome to while for loop {count} times!"
        messages.append(msg)
        print(msg)
    return messages


def demo_while_for(override_count: Optional[int] = 3) -> List[str]:
    """Run interactive or automated demonstration of while-for loop orchestration."""
    print("--- 1. Validating Input & Executing Iteration Loop ---")
    n = override_count if override_count is not None else validate_positive_number(3)
    return repeat_greeting_loop(n)


if __name__ == "__main__":
    demo_while_for()
