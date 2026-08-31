"""Dynamic Value Truthiness and Registration Validation.

Demonstrates how dynamic state variables (Booleans, None, Numbers, Containers)
behave when evaluated directly in conditional statements.

Import Notes:
    - 'from typing import Any, List, Tuple': Standard library typing imports for annotating
      dynamic data types, list structures, and tuple pairs.
"""

from typing import Any, List, Tuple


def is_user_registered(registration_state: Any) -> bool:
    """Return True if registration_state evaluates to Truthy in Python."""
    if registration_state:
        return True
    else:
        return False


def demo_more_if() -> None:
    """Demonstrate state evaluation across diverse types."""
    test_states: List[Tuple[str, Any]] = [
        ("Boolean False", False),
        ("None Object", None),
        ("Integer Zero", 0),
        ("Positive Integer", 2),
        ("Empty String", ""),
        ("Empty Tuple", ()),
        ("Empty List", []),
        ("Empty Dict", {}),
        ("Empty Set", set()),
        ("Populated List", ["Alice", "Bob"]),
    ]

    print("--- User Registration State Evaluation ---")
    for description, state in test_states:
        registered = is_user_registered(state)
        print(f"State: {description:18s} | Representation: {repr(state):15s} -> Registered: {registered}")


if __name__ == "__main__":
    demo_more_if()
