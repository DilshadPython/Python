"""
Cryptographically Secure Password Generator & Logger Module.

This module provides enterprise-grade, cryptographically secure password generation
using Python's standard `secrets` module (PEP 506), alongside timestamped log persistence.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import datetime`: Standard library module for generating timestamped entry headers.
# - `from pathlib import Path`: Object-oriented filesystem path handling (PEP 428).
# - `import secrets`: Cryptographically strong random number generation for security (PEP 506).
# - `import string`: Constant string character sets (ascii_lowercase, ascii_uppercase, digits, punctuation).
# - `import sys`: System interaction and process exit code propagation.
# - `from typing import Optional`: PEP 484 type annotations for optional argument types.
# =========================================================================
import datetime
from pathlib import Path
import secrets
import string
import sys
from typing import Optional


# Constant default character pools
LOWERCASE_CHARS: str = string.ascii_lowercase
UPPERCASE_CHARS: str = string.ascii_uppercase
DIGIT_CHARS: str = string.digits
SYMBOL_CHARS: str = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

ALL_CHARACTER_POOL: str = LOWERCASE_CHARS + UPPERCASE_CHARS + DIGIT_CHARS + SYMBOL_CHARS


def generate_secure_password(length: int = 16) -> str:
    """Generate a cryptographically secure random password of specified length.

    Guarantees at least one character from each character category (lowercase,
    uppercase, digit, symbol) and uses `secrets.choice` for cryptographic safety.

    Args:
        length (int): Desired password length. Defaults to 16. Minimum length is 8.

    Returns:
        str: Generated secure password.

    Raises:
        TypeError: If length is not an integer.
        ValueError: If length is less than 8.
    """
    if not isinstance(length, int):
        raise TypeError(f"Password length must be an integer, got {type(length).__name__}")
    if length < 8:
        raise ValueError(f"Password length must be at least 8 characters, got {length}")

    # Ensure at least one character from each character pool for strong entropy
    password_chars = [
        secrets.choice(LOWERCASE_CHARS),
        secrets.choice(UPPERCASE_CHARS),
        secrets.choice(DIGIT_CHARS),
        secrets.choice(SYMBOL_CHARS),
    ]

    # Fill remaining password length from full character pool
    for _ in range(length - 4):
        password_chars.append(secrets.choice(ALL_CHARACTER_POOL))

    # Cryptographically shuffle character positions
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def save_password_log(
    password: str,
    log_file_path: str | Path = "gmail.txt",
    service_name: Optional[str] = None,
) -> Path:
    """Append a timestamped password entry to a specified log file.

    Args:
        password (str): Password string to persist.
        log_file_path (str | Path): Target log file path. Defaults to "gmail.txt".
        service_name (Optional[str]): Optional service label for log header.

    Returns:
        Path: Path object pointing to the written log file.

    Raises:
        ValueError: If password string is empty.
    """
    if not password:
        raise ValueError("Cannot log an empty password string")

    target_path = Path(log_file_path)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    label = f"[{service_name.upper()}] " if service_name else ""
    log_entry = f"{current_time}: {label}{password}\n"

    # Use context manager for safe file I/O operations
    with target_path.open("a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

    return target_path


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for password generator module.

    Args:
        argv (list[str] | None): Command line arguments. Defaults to sys.argv[1:].

    Returns:
        int: Status exit code (0 for success, non-zero for failure).
    """
    if argv is None:
        argv = sys.argv[1:]

    print("=== Cryptographically Secure Password Generator ===")
    
    length = 16
    if argv:
        try:
            length = int(argv[0])
        except ValueError:
            print(f"Error: Invalid length argument '{argv[0]}'. Please provide an integer.")
            return 1

    try:
        password = generate_secure_password(length)
    except (TypeError, ValueError) as err:
        print(f"Error generating password: {err}")
        return 1

    print(f"Generated Password ({len(password)} chars): {password}")

    # Prompt user for service log choice or default to gmail.txt
    log_filename = "gmail.txt"
    log_path = save_password_log(password, log_file_path=log_filename)
    print(f"Successfully appended entry to log file: {log_path.resolve()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
