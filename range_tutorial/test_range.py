"""Unit Test Suite for the Range Module.

This test suite verifies all functions across range_basics, range_formatting,
number_formatting, datetime_formatting, graphics_3d, and range_vs_xrange modules,
ensuring strict compliance with expected inputs, outputs, and defensive error handling.
"""

import datetime
import unittest

# Import functions from Range module scripts
from range_basics import (
    format_grid,
    format_horizontal_sequence,
    generate_sequence,
)
from range_formatting import format_range_numbers
from number_formatting import format_float_precision, format_large_number
from datetime_formatting import format_datetime_detailed, format_datetime_standard
from graphics_3d import (
    generate_ascii_pyramid,
    generate_decreasing_space_pattern,
    generate_single_sided_pyramid,
)
from range_vs_xrange import (
    compare_range_memory_and_type,
    demonstrate_range_attributes,
    demonstrate_range_sequence_methods,
    introspect_range_attributes_and_methods,
)


class TestRangeBasics(unittest.TestCase):
    """Test suite for range_basics.py module."""

    def test_generate_sequence_valid(self) -> None:
        """Verify basic sequence generation with start, stop, and step."""
        self.assertEqual(generate_sequence(0, 5), [0, 1, 2, 3, 4])
        self.assertEqual(generate_sequence(10, 20, 2), [10, 12, 14, 16, 18])
        self.assertEqual(generate_sequence(10, 0, -2), [10, 8, 6, 4, 2])

    def test_generate_sequence_type_error(self) -> None:
        """Verify TypeError when invalid parameter types are passed."""
        with self.assertRaises(TypeError):
            generate_sequence("0", 5)  # type: ignore

    def test_generate_sequence_value_error(self) -> None:
        """Verify ValueError when step is zero."""
        with self.assertRaises(ValueError):
            generate_sequence(0, 10, 0)

    def test_format_grid(self) -> None:
        """Verify nested grid generation."""
        grid = format_grid(2, 3)
        self.assertEqual(len(grid), 2)
        self.assertEqual(grid[0], "0x0y  0x1y  0x2y")
        self.assertEqual(grid[1], "1x0y  1x1y  1x2y")

    def test_format_grid_errors(self) -> None:
        """Verify grid input validation."""
        with self.assertRaises(TypeError):
            format_grid("2", 3)  # type: ignore
        with self.assertRaises(ValueError):
            format_grid(0, 3)

    def test_format_horizontal_sequence(self) -> None:
        """Verify horizontal sequence formatting."""
        res = format_horizontal_sequence(0, 5)
        self.assertEqual(res, "0 1 2 3 4")


class TestRangeFormatting(unittest.TestCase):
    """Test suite for range_formatting.py module."""

    def test_format_range_numbers_padded(self) -> None:
        """Verify zero-padded line generation."""
        lines = format_range_numbers(1, 4, width=3, prefix="No.")
        self.assertEqual(lines, ["No. 001", "No. 002", "No. 003"])

    def test_format_range_numbers_errors(self) -> None:
        """Verify parameter validation."""
        with self.assertRaises(TypeError):
            format_range_numbers(1, 4, width="3")  # type: ignore
        with self.assertRaises(ValueError):
            format_range_numbers(1, 4, width=0)


class TestNumberFormatting(unittest.TestCase):
    """Test suite for number_formatting.py module."""

    def test_format_float_precision(self) -> None:
        """Verify float precision formatting."""
        self.assertEqual(format_float_precision(3.14159, 2), "The Pi is = 3.14")
        self.assertEqual(format_float_precision(3.14159, 4), "The Pi is = 3.1416")

    def test_format_float_errors(self) -> None:
        """Verify precision argument type/value checks."""
        with self.assertRaises(TypeError):
            format_float_precision("3.14")  # type: ignore
        with self.assertRaises(ValueError):
            format_float_precision(3.14, -1)

    def test_format_large_number(self) -> None:
        """Verify thousand separator formatting."""
        self.assertEqual(format_large_number(1000000, ""), "1,000,000")
        self.assertEqual(format_large_number(1073741824, "Byte"), "1,073,741,824 Byte")


class TestDatetimeFormatting(unittest.TestCase):
    """Test suite for datetime_formatting.py module."""

    def test_format_datetime_standard(self) -> None:
        """Verify standard datetime formatting output."""
        dt = datetime.datetime(2026, 1, 30, 3, 20, 33)
        res = format_datetime_standard(dt)
        self.assertEqual(res, "I wrote this code January 30, 2026, 03:20:33")

    def test_format_datetime_detailed(self) -> None:
        """Verify detailed datetime formatting including day of week and year."""
        dt = datetime.datetime(2026, 1, 30, 3, 20, 33)
        res = format_datetime_detailed(dt)
        self.assertIn("Friday", res)
        self.assertIn("030", res)

    def test_format_datetime_errors(self) -> None:
        """Verify validation on datetime inputs."""
        with self.assertRaises(TypeError):
            format_datetime_standard("2026-01-30")  # type: ignore


class TestGraphics3D(unittest.TestCase):
    """Test suite for graphics_3d.py module."""

    def test_generate_decreasing_space_pattern(self) -> None:
        """Verify decreasing space line count and format."""
        lines = generate_decreasing_space_pattern(5)
        self.assertEqual(len(lines), 5)
        self.assertTrue(lines[0].endswith("#"))

    def test_generate_single_sided_pyramid(self) -> None:
        """Verify single-sided pyramid generation."""
        lines = generate_single_sided_pyramid(3)
        self.assertEqual(len(lines), 3)
        self.assertTrue(lines[0].endswith("0"))
        self.assertTrue(lines[2].endswith("000"))

    def test_generate_ascii_pyramid(self) -> None:
        """Verify symmetric 3D pyramid width progression."""
        lines = generate_ascii_pyramid(3)
        self.assertEqual(len(lines), 3)
        # Check odd block progression (1, 3, 5)
        self.assertEqual(lines[0].strip(), "0")
        self.assertEqual(lines[1].strip(), "000")
        self.assertEqual(lines[2].strip(), "00000")


class TestRangeVsXRange(unittest.TestCase):
    """Test suite for range_vs_xrange.py comparative module."""

    def test_compare_range_memory(self) -> None:
        """Verify constant memory sizing for range objects."""
        info_small = compare_range_memory_and_type(100)
        info_large = compare_range_memory_and_type(1_000_000)
        self.assertEqual(info_small["range_memory_bytes"], info_large["range_memory_bytes"])

    def test_demonstrate_range_attributes(self) -> None:
        """Verify range attributes start, stop, and step."""
        attrs = demonstrate_range_attributes(2, 20, 3)
        self.assertEqual(attrs["start"], 2)
        self.assertEqual(attrs["stop"], 20)
        self.assertEqual(attrs["step"], 3)

    def test_demonstrate_range_sequence_methods(self) -> None:
        """Verify sequence methods .index(), .count() and containment."""
        rng = range(10, 50, 5)
        res_contained = demonstrate_range_sequence_methods(rng, 20)
        self.assertTrue(res_contained["is_contained"])
        self.assertEqual(res_contained["index"], 2)
        self.assertEqual(res_contained["count"], 1)

        res_missing = demonstrate_range_sequence_methods(rng, 22)
        self.assertFalse(res_missing["is_contained"])
        self.assertIsNone(res_missing["index"])
        self.assertEqual(res_missing["count"], 0)

    def test_introspect_range_attributes(self) -> None:
        """Verify dir(range) output contains core range methods."""
        attributes = introspect_range_attributes_and_methods()
        self.assertIn("start", attributes)
        self.assertIn("stop", attributes)
        self.assertIn("step", attributes)
        self.assertIn("index", attributes)
        self.assertIn("count", attributes)
        self.assertIn("__contains__", attributes)


if __name__ == "__main__":
    unittest.main()
