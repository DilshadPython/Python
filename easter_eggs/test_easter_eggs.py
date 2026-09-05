"""
Unittest Suite for Python Easter Eggs Module (`easter_eggs`)
"""
import unittest
from easter_eggs.import_this_zen_of_python import (
    get_zen_text,
    get_encoded_text,
    get_cipher_map,
)
from easter_eggs.import_antigravity_xkcd import calculate_geohash
from easter_eggs.import_future_braces import demonstrate_braces_import
from easter_eggs.import_hello_world import capture_hello_output
from easter_eggs.import_future_flufl import (
    demonstrate_flufl_ne_error,
    demonstrate_flufl_diamond_op,
)


class TestEasterEggs(unittest.TestCase):
    """Test case suite covering all Python Easter egg scripts."""

    def test_this_zen_of_python(self) -> None:
        """Tests `import this` output and dictionary attributes."""
        zen_text = get_zen_text()
        self.assertIn("The Zen of Python, by Tim Peters", zen_text)
        self.assertIn("Beautiful is better than ugly.", zen_text)

        encoded = get_encoded_text()
        self.assertGreater(len(encoded), 100)

        cipher_map = get_cipher_map()
        self.assertEqual(cipher_map.get("a"), "n")
        self.assertEqual(cipher_map.get("n"), "a")

    def test_antigravity_geohash(self) -> None:
        """Tests `antigravity.geohash` output generation."""
        # Check that calculate_geohash runs cleanly without raising exceptions
        calculate_geohash(37.421542, -122.085589, b"2005-05-26-10458.68")

    def test_future_braces(self) -> None:
        """Tests `from __future__ import braces` raises SyntaxError('not a chance')."""
        err_msg = demonstrate_braces_import()
        self.assertIn("not a chance", err_msg)

    def test_hello_world(self) -> None:
        """Tests `import __hello__` output."""
        output = capture_hello_output()
        self.assertEqual(output, "Hello world!")

    def test_future_flufl(self) -> None:
        """Tests `from __future__ import barry_as_FLUFL` PEP 401 behavior."""
        err_msg = demonstrate_flufl_ne_error()
        self.assertIn("use '<>' instead of '!='", err_msg)
        self.assertTrue(demonstrate_flufl_diamond_op())


if __name__ == "__main__":
    unittest.main()
