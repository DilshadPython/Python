"""Logical 'and' Operator and Short-Circuit Evaluation.

Demonstrates the boolean 'and' operator.
In Python, 'A and B' evaluates expression A first. If A is False, Python
short-circuits (skips evaluation of B) and immediately returns False.

Import Notes:
    - 'from typing import List, Tuple': Standard library typing module imports
      to annotate list parameters and tuples containing user role test cases.
"""

from typing import List, Tuple


def verify_user_access(user_role: str, is_registered: bool) -> bool:
    """Verify if a user has access based on role AND registration status."""
    # Both conditions must evaluate to True for the block to return True.
    if user_role == "Student" and is_registered:
        return True
    return False


def demo_if_and() -> None:
    """Demonstrate logical AND access validation."""
    print("--- Testing Logical AND Access ---")
    test_cases: List[Tuple[str, bool]] = [
        ("Student", True),
        ("Student", False),
        ("Guest", True),
        ("Guest", False),
    ]

    for role, registered in test_cases:
        granted = verify_user_access(role, registered)
        status_str = "Access Granted" if granted else "Access Denied"
        print(f"Role: {role:8s} | Registered: {str(registered):5s} -> {status_str}")


if __name__ == "__main__":
    demo_if_and()
