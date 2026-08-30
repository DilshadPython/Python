"""Unit Test Suite for Object Composition Module.

This module provides unittest coverage for Object Composition and dependency injection.
"""

import io
import unittest
from object_composition import TextComposer


class TestObjectComposition(unittest.TestCase):
    """Unit tests verifying object composition with in-memory streams."""

    def test_text_composer_with_string_io(self) -> None:
        """Verify TextComposer correctly delegates writing to io.StringIO."""
        stream = io.StringIO()
        composer = TextComposer(stream)
        composer.write_message("Test composition message")
        self.assertEqual(stream.getvalue(), "Test composition message")


if __name__ == "__main__":
    unittest.main()
