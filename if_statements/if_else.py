"""Basic 'if-else' Branching Logic.

Demonstrates simple dual-branch selection: executes the 'if' block when True,
or falls back to the 'else' block when False.

Import Notes:
    - 'from typing import Union': Standard library typing module import for annotations.
"""

from typing import Union


def verify_technology(tech_name: str) -> bool:
    """Check if the provided technology string matches expected target."""
    if tech_name == "Hello Python":
        return True
    else:
        return False


def demo_if_else() -> None:
    """Run basic if-else string verification."""
    target_tech = "Hello Python"
    is_valid = verify_technology(target_tech)
    print(f"Technology String '{target_tech}' matches target: {is_valid}")


if __name__ == "__main__":
    demo_if_else()
