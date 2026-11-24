"""Unit Test Suite for String Formatting Operations.

Validates percent (%) formatting, str.format(), f-strings, string.Template, and type conversions.
"""

import math
import unittest
from datetime import datetime

from f_strings_ops import (
    format_f_string_basics,
    format_f_string_debug,
    format_f_string_expressions,
    format_f_string_specifiers,
)
from percent_formatting_ops import (
    format_numbers_with_percent,
    format_with_dict_percent,
    format_with_percent_s_and_r,
)
from str_format_ops import (
    format_alignment_and_padding,
    format_index_and_attribute,
    format_number_commas_and_percents,
    format_positional_and_keyword,
)
from template_strings_ops import (
    custom_delimiter_template,
    safe_substitute_template,
    substitute_template,
)
from type_conversion_ops import (
    convert_int_and_float_strings,
    convert_to_string,
    get_string_representation,
    inspect_variable_type,
)


class TestFormatStringsModule(unittest.TestCase):
    """Test suite covering string formatting techniques."""

    def test_percent_formatting(self) -> None:
        """Test %-style formatting methods."""
        res_sr = format_with_percent_s_and_r("Python", 3.12)
        self.assertIn("Name (str): Python", res_sr)
        self.assertIn("Value (repr): 3.12", res_sr)

        num_formatted = format_numbers_with_percent(234.3456, width=1, precision=2)
        self.assertEqual(num_formatted, "234.35")

        dict_res = format_with_dict_percent({"first_name": "A", "last_name": "B", "age": 20})
        self.assertEqual(dict_res, "User A B is 20 years old.")

    def test_str_format(self) -> None:
        """Test str.format() methods."""
        pos_kw = format_positional_and_keyword("Alice", 25, city="Paris")
        self.assertEqual(pos_kw, "Hello Alice! You are 25 years old and live in Paris.")

        idx_attr = format_index_and_attribute((30, 175), math)
        self.assertIn("User age=30", idx_attr)
        self.assertIn("pi=3.1415", idx_attr)

        aligned = format_alignment_and_padding("Test", width=10, align_char="^", fill_char="-")
        self.assertEqual(aligned, "---Test---")

        commas = format_number_commas_and_percents(1234567.89)
        self.assertIn("$1,234,567.89", commas)

    def test_f_strings(self) -> None:
        """Test f-string operations."""
        basics = format_f_string_basics("David", "Smith")
        self.assertEqual(basics, "David [Smith] is a Python Developer.")

        expr = format_f_string_expressions(10, 5)
        self.assertIn("Sum of 10 + 5 = 15", expr)

        dbg = format_f_string_debug(100, "active")
        self.assertEqual(dbg, "Debugging: var1=100 | var2='active'")

        dt = datetime(2026, 9, 5, 21, 0, 0)
        spec = format_f_string_specifiers(1000.5, dt)
        self.assertIn("$1,000.50", spec)
        self.assertIn("2026-09-05 21:00", spec)

    def test_template_strings(self) -> None:
        """Test string.Template substitution."""
        sub = substitute_template("Hello $name", {"name": "World"})
        self.assertEqual(sub, "Hello World")

        safe = safe_substitute_template("Hello $name $missing", {"name": "World"})
        self.assertEqual(safe, "Hello World $missing")

        custom = custom_delimiter_template("Hi %user", {"user": "Alice"})
        self.assertEqual(custom, "Hi Alice")

    def test_type_conversions(self) -> None:
        """Test type conversion and inspection methods."""
        self.assertEqual(convert_to_string(123), "123")
        self.assertEqual(get_string_representation("hello\n"), "'hello\\n'")

        info = inspect_variable_type([1, 2])
        self.assertEqual(info["type_name"], "list")
        self.assertTrue(info["is_list"])

        i_val, f_val = convert_int_and_float_strings("99.9")
        self.assertEqual(i_val, 99)
        self.assertEqual(f_val, 99.9)


if __name__ == "__main__":
    unittest.main()
