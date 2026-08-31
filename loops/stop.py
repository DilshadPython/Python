"""Demonstration of Python Loop Keywords: 'break', 'continue', and 'pass'.

Exemplifies control flow mechanics during sequence iteration:
    - 'break': Terminates loop execution immediately.
    - 'continue': Skips remaining statements in current iteration step.
    - 'pass': Syntactic placeholder that performs no operation.

Import Notes:
    - 'from typing import List, Tuple': Standard library typing imports for list and tuple type hints.
"""

from typing import List, Tuple


def evaluate_loop_keywords(
    data: List[str], target: str = "STOP", skip: str = "SKIP"
) -> Tuple[List[str], str]:
    """Process a list of tokens demonstrating 'break', 'continue', and 'pass'.

    Args:
        data: List of string tokens.
        target: Token value that triggers 'break' loop termination.
        skip: Token value that triggers 'continue' step bypass.

    Returns:
        Tuple containing list of processed tokens and final completion state message.
    """
    processed: List[str] = []
    final_state = "COMPLETED_NORMALLY"

    for item in data:
        if item == target:
            print(f"Target '{target}' encountered! Executing 'break'.")
            final_state = f"BROKEN_AT_{target}"
            break
        elif item == skip:
            print(f"Skip token '{skip}' encountered! Executing 'continue'.")
            continue
        else:
            print(f"Processing item '{item}' -> Executing 'pass'.")
            processed.append(item)
            pass

    return processed, final_state


def demo_stop() -> Tuple[List[str], str]:
    """Run demonstration of break, continue, and pass loop keywords."""
    sample_data = ["alpha", "SKIP", "beta", "gamma", "STOP", "delta"]
    print("--- Demonstrating 'break', 'continue', and 'pass' ---")
    processed, state = evaluate_loop_keywords(sample_data, "STOP", "SKIP")
    print(f"Processed Tokens: {processed} | Loop State: {state}")
    return processed, state


if __name__ == "__main__":
    demo_stop()