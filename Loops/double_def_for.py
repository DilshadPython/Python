"""Modular Function Calls Passing Input Parameters into 'for' Loops.

Demonstrates modular function orchestration where an input validation function
passes a validated number into a worker function executing a 'for' loop.

Import Notes:
    - 'from typing import List': Standard library typing import for string list annotations.
"""

from typing import List


def execute_repeated_greeting(repetitions: int) -> List[str]:
    """Execute a 'for' loop to generate greeting messages 'repetitions' times."""
    greeting_records: List[str] = []
    for step in range(repetitions):
        record = f"Step {step}: Welcome to Python"
        greeting_records.append(record)
        print(record)
    return greeting_records


def demo_double_def_for() -> None:
    """Demonstrate modular function execution with 3 repetitions."""
    print("--- Demonstrating Modular Function 'for' Loop Execution ---")
    target_count = 3
    results = execute_repeated_greeting(target_count)
    print(f"Completed execution of {len(results)} steps.")


if __name__ == "__main__":
    demo_double_def_for()
