"""
Unit Test Suite for `unicode_names.py` and `uuid_generator.py`.

This module tests:
1. Unicode character name lookup and category resolution.
2. Reverse character lookup by Unicode name.
3. RFC 4122 UUID generation (v1, v3, v4, v5) and version property verification.
"""

import unittest
import uuid

# Support both package and local directory import paths
try:
    from unicode_strings.unicode_names import (
        get_character_metadata,
        lookup_character_by_name,
        inspect_symbol_suite,
    )
    from unicode_strings.uuid_generator import (
        generate_uuid_v1,
        generate_uuid_v3,
        generate_uuid_v4,
        generate_uuid_v5,
    )
except ImportError:
    from unicode_names import (
        get_character_metadata,
        lookup_character_by_name,
        inspect_symbol_suite,
    )
    from uuid_generator import (
        generate_uuid_v1,
        generate_uuid_v3,
        generate_uuid_v4,
        generate_uuid_v5,
    )


class TestUnicodeNames(unittest.TestCase):
    """Test suite verifying Unicode character inspection functions."""

    def test_get_character_metadata_valid(self) -> None:
        """Verify metadata fields for Euro sign and Ampersand."""
        euro_meta = get_character_metadata("€")
        self.assertEqual(euro_meta["symbol"], "€")
        self.assertEqual(euro_meta["name"], "EURO SIGN")
        self.assertEqual(euro_meta["codepoint"], "U+20AC")

        amp_meta = get_character_metadata("&")
        self.assertEqual(amp_meta["name"], "AMPERSAND")

    def test_get_character_metadata_errors(self) -> None:
        """Verify TypeError and ValueError handling."""
        with self.assertRaises(TypeError):
            get_character_metadata(123)  # type: ignore
        with self.assertRaises(ValueError):
            get_character_metadata("AB")

    def test_lookup_character_by_name(self) -> None:
        """Verify character resolution from official Unicode name."""
        char = lookup_character_by_name("POUND SIGN")
        self.assertEqual(char, "£")

    def test_lookup_character_by_name_invalid(self) -> None:
        """Verify KeyError for non-existent Unicode name."""
        with self.assertRaises(KeyError):
            lookup_character_by_name("NON_EXISTENT_UNICODE_CHARACTER_XYZ")

    def test_inspect_symbol_suite(self) -> None:
        """Verify inspection suite returns correct list length."""
        results = inspect_symbol_suite(["$", "%"])
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["name"], "DOLLAR SIGN")
        self.assertEqual(results[1]["name"], "PERCENT SIGN")


class TestUUIDGenerator(unittest.TestCase):
    """Test suite verifying RFC 4122 UUID generation functions."""

    def test_generate_uuid_v1(self) -> None:
        """Verify UUID v1 generation and version code."""
        uuids = generate_uuid_v1(3)
        self.assertEqual(len(uuids), 3)
        for u in uuids:
            self.assertEqual(u.version, 1)

    def test_generate_uuid_v3(self) -> None:
        """Verify UUID v3 MD5 namespace generation determinism."""
        u1 = generate_uuid_v3("python.org")
        u2 = generate_uuid_v3("python.org")
        self.assertEqual(u1, u2)
        self.assertEqual(u1.version, 3)

    def test_generate_uuid_v4(self) -> None:
        """Verify UUID v4 random generation and version code."""
        uuids = generate_uuid_v4(5)
        self.assertEqual(len(uuids), 5)
        for u in uuids:
            self.assertEqual(u.version, 4)

    def test_generate_uuid_v5(self) -> None:
        """Verify UUID v5 SHA-1 namespace generation determinism."""
        u1 = generate_uuid_v5("python.org")
        u2 = generate_uuid_v5("python.org")
        self.assertEqual(u1, u2)
        self.assertEqual(u1.version, 5)

    def test_uuid_errors(self) -> None:
        """Verify parameter validation for count and names."""
        with self.assertRaises(TypeError):
            generate_uuid_v1("invalid")  # type: ignore
        with self.assertRaises(ValueError):
            generate_uuid_v4(0)


if __name__ == "__main__":
    unittest.main()
