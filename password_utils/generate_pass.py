"""
Legacy Compatibility Wrapper for Password Generation.

This module provides a backward-compatible wrapper script that imports core functions
from `password_generator.py`, correcting legacy spelling errors, unclosed file handlers,
and unsafe random generation algorithms.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI argument propagation.
# - `from password_generator import generate_secure_password, save_password_log`:
#   Core cryptographically secure generation and persistence functions.
# =========================================================================
import sys

# Try package or local module import
try:
    from password_utils.password_generator import (
        generate_secure_password,
        save_password_log,
    )
except ImportError:
    from password_generator import (
        generate_secure_password,
        save_password_log,
    )


def interactive_password_generation() -> str:
    """Prompt user for password length and log generated password securely."""
    try:
        user_input = input("Enter length of password: ").strip()
        length = int(user_input) if user_input else 16
    except ValueError:
        print("Invalid input. Defaulting password length to 16.")
        length = 16

    password = generate_secure_password(length)
    print("Generated new password:", password)

    # Persist entry to gmail.txt using context manager inside save_password_log
    log_path = save_password_log(password, log_file_path="gmail.txt")
    print(f"Password logged to {log_path.name}")
    return password


if __name__ == "__main__":
    interactive_password_generation()