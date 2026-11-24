import unittest
from cloud_app.tutorials.string_basics import (
    reverse_string,
    format_user_greeting,
    extract_words
)

class TestStringsTutorial(unittest.TestCase):
    """Unit test suite for Strings tutorial module."""

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_reverse_string_invalid(self):
        with self.assertRaises(TypeError):
            reverse_string(12345)

    def test_format_user_greeting(self):
        self.assertEqual(format_user_greeting("dilshad"), "Welcome Dilshad (Developer)")

    def test_format_user_greeting_empty(self):
        with self.assertRaises(ValueError):
            format_user_greeting("")

    def test_extract_words(self):
        words = extract_words("Hello, Python 3 world!")
        self.assertEqual(words, ["Hello", "Python", "3", "world"])

if __name__ == "__main__":
    unittest.main()
