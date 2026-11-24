"""Email Validation Demonstration Module.

This module provides clear, PEP 8-compliant regular expression functions to validate
email addresses. It demonstrates character classes, quantifier syntax, domain name
matching, optional top-level domains (TLDs), and case-insensitive flags.
"""

# import standard re module for regular expression pattern matching
import re
from typing import Optional, Match

# Compiled regex pattern for validating email addresses:
# - ^\w+([\.-]?\w+)* : Username starts with word chars, allowing optional dots/hyphens
# - @\w+([\.-]?\w+)* : Domain name after @ symbol
# - \.[a-zA-Z]{2,}$  : Top-level domain (TLD) requiring at least 2 alpha characters
EMAIL_PATTERN: re.Pattern = re.compile(
    r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*\.[a-zA-Z]{2,}$",
    re.IGNORECASE,
)


def validate_email(email: str) -> bool:
    """Validate whether an email string matches standard email formatting.

    Args:
        email: The raw email address string to validate.

    Returns:
        True if the email matches valid structural rules, False otherwise.
    """
    if not email or not isinstance(email, str):
        return False
    return bool(EMAIL_PATTERN.fullmatch(email.strip()))


def extract_email_parts(email: str) -> Optional[tuple[str, str]]:
    """Extract the username and domain parts from a valid email address.

    Args:
        email: Email address string to parse.

    Returns:
        A tuple of (username, domain) if valid, or None if invalid.
    """
    pattern = re.compile(r"^([\w\.-]+)@([\w\.-]+\.[a-zA-Z]{2,})$", re.IGNORECASE)
    match: Optional[Match] = pattern.match(email.strip())
    if match:
        return match.group(1), match.group(2)
    return None


if __name__ == "__main__":
    print("=== Email Validation Demonstration ===")
    
    sample_emails = [
        "user@example.com",
        "john.doe@teach-cloud.net",
        "alice_smith123@sub.domain.co.uk",
        "invalid-email@",
        "@domain.com",
        "user@domain",
    ]

    for sample in sample_emails:
        is_valid = validate_email(sample)
        parts = extract_email_parts(sample)
        print(f"Email: '{sample}' -> Valid: {is_valid} | Parts: {parts}")
