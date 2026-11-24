"""Password Strength Validation using if-else.

Demonstrates evaluating string length in conditional checks to enforce simple security rules.

Import Notes:
    - 'from typing import List': Standard library typing module import to type-annotate
      password list data.
"""

from typing import List


def validate_password_strength(password: str) -> str:
    """Evaluate password strength based on character count threshold."""
    if len(password) >= 8:
        return "Strong Password"
    else:
        return "Weak Password (Minimum 8 characters required)"


def demo_if_else_1() -> None:
    """Run password validation demonstration."""
    passwords: List[str] = ["secret", "SecureP@ss2026", "12345"]
    for pwd in passwords:
        assessment = validate_password_strength(pwd)
        print(f"Password: '{pwd:15s}' -> {assessment}")


if __name__ == "__main__":
    demo_if_else_1()
