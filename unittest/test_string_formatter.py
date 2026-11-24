"""
Unit test suite for string_formatter module testing welcome message formatting,
number squaring, and type error handling.
"""
# "import module" loads unittest from standard library.
import unittest
# "from module import name" imports string formatting functions into test scope.
from string_formatter import format_welcome_message, square_number


class TestStringFormatter(unittest.TestCase):
    """Test suite covering greeting formatting and number squaring functions."""

    def test_default_welcome_message(self):
        """Test format_welcome_message default parameter behavior."""
        self.assertEqual(format_welcome_message(), "Welcome back to, Python")

    def test_custom_welcome_message(self):
        """Test format_welcome_message with custom arguments."""
        self.assertEqual(format_welcome_message("Django"), "Welcome back to, Django")
        for tech in ["Flask", "FastAPI", "React", "Docker"]:
            with self.subTest(tech=tech):
                self.assertEqual(format_welcome_message(tech), f"Welcome back to, {tech}")

    def test_square_number_positive_and_negative(self):
        """Test squaring positive, negative, and zero integers."""
        self.assertEqual(square_number(2), 4)
        self.assertEqual(square_number(3), 9)
        self.assertEqual(square_number(-2), 4)
        self.assertEqual(square_number(-3), 9)
        self.assertEqual(square_number(0), 0)

    def test_square_number_invalid_type(self):
        """Verify TypeError is raised when passing string or boolean to square_number."""
        with self.assertRaises(TypeError):
            square_number("Django")
        with self.assertRaises(TypeError):
            square_number(True)


if __name__ == '__main__':
    unittest.main()
