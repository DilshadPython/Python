"""Legacy Email Validation Script (Refactored).

This module updates the original `valid_email.py` into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For modular functions and comprehensive educational references, see `email_validator.py`.
"""

# import standard re module and helper function from email_validator
import re
from email_validator import validate_email


def check_email_interactive(email_input: str) -> str:
    """Validate an email input string and return a user-friendly status message.

    Args:
        email_input: Raw email string to validate.

    Returns:
        'Valid Email' if valid, or 'Invalid Email' if invalid.
    """
    if validate_email(email_input):
        return "Valid Email"
    return "Invalid Email"


if __name__ == "__main__":
    print("=== Legacy Email Validator (Refactored) ===")
    test_address = "user@example.com"
    result = check_email_interactive(test_address)
    print(f"Address: '{test_address}' -> Result: {result}")
