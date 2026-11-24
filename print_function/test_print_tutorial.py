import io
import sys
import unittest
from cloud_app.tutorials.print_basics import (
    format_simple_message,
    format_multi_line,
    print_to_stream
)

class TestPrintTutorial(unittest.TestCase):
    """Unit test suite for 1.Print tutorial module."""

    def test_format_simple_message_valid(self):
        """Test formatting valid string messages."""
        self.assertEqual(format_simple_message("Hello Python"), "Hello Python")

    def test_format_simple_message_invalid_type(self):
        """Test that non-string input raises a TypeError."""
        with self.assertRaises(TypeError):
            format_simple_message(12345)

    def test_format_multi_line(self):
        """Test joining multiple arguments into a formatted line."""
        result = format_multi_line("Python", 3, "Tutorial")
        self.assertEqual(result, "Python 3 Tutorial")

    def test_print_to_stream(self):
        """Test printing to an in-memory stream buffer."""
        buffer = io.StringIO()
        print_to_stream(buffer, "Testing output stream", end="\n")
        self.assertEqual(buffer.getvalue(), "Testing output stream\n")

    def test_python_fundamentals_route(self):
        """Test that /python-fundamentals renders HTTP 200 OK."""
        from cloud_app import app
        with app.test_client() as client:
            response = client.get('/python-fundamentals')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Print &amp; Output Mechanics', response.data)

if __name__ == "__main__":
    unittest.main()

