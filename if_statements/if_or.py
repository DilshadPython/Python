"""Logical 'or' Operator and Short-Circuit Evaluation.

Demonstrates the boolean 'or' operator.
In Python, 'A or B' evaluates expression A first. If A is True, Python
short-circuits (skips evaluation of B) and immediately returns True.

Import Notes:
    - 'from typing import List, Tuple': Standard library typing module imports
      for annotating lists and tuple test case pairs.
"""

from typing import List, Tuple


def verify_any_permission(user_role: str, is_admin: bool) -> bool:
    """Check if permission is granted if EITHER role is 'Student' OR user is Admin."""
    if user_role == "Student" or is_admin:
        return True
    return False


def demo_if_or() -> None:
    """Run logical OR authorization test cases."""
    print("--- Testing Logical OR Permission ---")
    test_cases: List[Tuple[str, bool]] = [
        ("Student", False),
        ("Guest", True),
        ("Guest", False),
    ]

    for role, admin_status in test_cases:
        permitted = verify_any_permission(role, admin_status)
        print(f"Role: {role:8s} | Is Admin: {str(admin_status):5s} -> Permitted: {permitted}")


if __name__ == "__main__":
    demo_if_or()
