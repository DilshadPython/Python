"""
Unit Test Suite for Password Generator Module (`password_generator.py`).

This module verifies:
1. Cryptographically secure password generation character set rules.
2. Boundary validation and defensive type/value error handling.
3. File logging persistence using temporary test file fixtures.
"""

from pathlib import Path
import string
import tempfile
import unittest

# Support both package and local directory import paths
try:
    from password_utils.password_generator import (
        generate_secure_password,
        save_password_log,
        LOWERCASE_CHARS,
        UPPERCASE_CHARS,
        DIGIT_CHARS,
        SYMBOL_CHARS,
    )
except ImportError:
    from password_generator import (
        generate_secure_password,
        save_password_log,
        LOWERCASE_CHARS,
        UPPERCASE_CHARS,
        DIGIT_CHARS,
        SYMBOL_CHARS,
    )


class TestPasswordGenerator(unittest.TestCase):
    """Test suite verifying password generation and logging operations."""

    def test_password_length_default(self) -> None:
        """Verify default password length is 16 characters."""
        password = generate_secure_password()
        self.assertEqual(len(password), 16)

    def test_password_custom_length(self) -> None:
        """Verify password generation with custom length boundaries."""
        for length in [8, 20, 64, 128]:
            password = generate_secure_password(length)
            self.assertEqual(len(password), length)

    def test_password_character_diversity(self) -> None:
        """Verify generated password contains at least one character from each pool."""
        password = generate_secure_password(24)
        has_lower = any(c in LOWERCASE_CHARS for c in password)
        has_upper = any(c in UPPERCASE_CHARS for c in password)
        has_digit = any(c in DIGIT_CHARS for c in password)
        has_symbol = any(c in SYMBOL_CHARS for c in password)

        self.assertTrue(has_lower, "Password must contain at least one lowercase character")
        self.assertTrue(has_upper, "Password must contain at least one uppercase character")
        self.assertTrue(has_digit, "Password must contain at least one numeric digit")
        self.assertTrue(has_symbol, "Password must contain at least one symbol character")

    def test_password_invalid_length_type(self) -> None:
        """Verify TypeError raised when non-integer length is provided."""
        with self.assertRaises(TypeError):
            generate_secure_password("16")  # type: ignore

    def test_password_invalid_length_value(self) -> None:
        """Verify ValueError raised when length is less than 8."""
        with self.assertRaises(ValueError):
            generate_secure_password(7)

    def test_save_password_log(self) -> None:
        """Verify save_password_log appends timestamped password entries to file."""
        with tempfile.TemporaryDirectory() as temp_dir:
            log_file = Path(temp_dir) / "test_log.txt"
            password = generate_secure_password(12)

            save_password_log(password, log_file_path=log_file, service_name="GMAIL")

            self.assertTrue(log_file.exists())
            content = log_file.read_text(encoding="utf-8")
            self.assertIn(password, content)
            self.assertIn("[GMAIL]", content)

    def test_save_password_log_empty_password(self) -> None:
        """Verify ValueError raised when attempting to log an empty password."""
        with self.assertRaises(ValueError):
            save_password_log("")


if __name__ == "__main__":
    unittest.main()
