"""Unit Test Suite for Fraction Module Operations.

Validates basics, conversions, arithmetic, rounding, and range evolution operations.
"""

import math
import unittest
from decimal import Decimal
from fractions import Fraction

from fraction_advanced_math_ops import (
    accumulate_fractions,
    apply_rounding_and_truncation,
    decimal_fraction_conversion_interop,
)
from fraction_arithmetic_ops import (
    calculate_fraction_divmod,
    compare_fractions,
    mixed_type_arithmetic,
    perform_fraction_arithmetic,
)
from fraction_basics_ops import (
    create_fraction_from_float_and_decimal,
    create_fraction_from_integers,
    create_fraction_from_string,
    inspect_fraction_components,
)
from fraction_conversions_ops import (
    approximate_float_to_fraction,
    compute_fraction_gcd,
    convert_fraction_to_numeric_types,
    extract_integer_ratio,
)
from fraction_range_evolution_ops import (
    compare_range_and_fraction_memory_efficiency,
    document_python_version_evolution,
    generate_fractional_range,
    inspect_range_attributes_and_methods,
)


class TestFractionBasics(unittest.TestCase):
    """Test cases for fraction instantiation and basic component inspection."""

    def test_create_from_integers_and_simplification(self) -> None:
        """Verify automatic GCD reduction when creating fractions from integers."""
        f = create_fraction_from_integers(4, 14)
        self.assertEqual(f.numerator, 2)
        self.assertEqual(f.denominator, 7)

    def test_zero_denominator_raises(self) -> None:
        """Verify ZeroDivisionError is raised on zero denominator."""
        with self.assertRaises(ZeroDivisionError):
            create_fraction_from_integers(1, 0)

    def test_create_from_string(self) -> None:
        """Verify parsing fraction strings including whitespace and decimals."""
        f1 = create_fraction_from_string(" 3 / 8 ")
        self.assertEqual(f1, Fraction(3, 8))

        f2 = create_fraction_from_string("0.75")
        self.assertEqual(f2, Fraction(3, 4))

    def test_create_from_float_and_decimal(self) -> None:
        """Verify creating Fraction objects from float and Decimal."""
        f_float = create_fraction_from_float_and_decimal(0.25)
        self.assertEqual(f_float, Fraction(1, 4))

        f_dec = create_fraction_from_float_and_decimal(Decimal("0.125"))
        self.assertEqual(f_dec, Fraction(1, 8))

    def test_inspect_components(self) -> None:
        """Verify numerator, denominator, and string component output dictionary."""
        info = inspect_fraction_components(Fraction(3, 4))
        self.assertEqual(info["numerator"], 3)
        self.assertEqual(info["denominator"], 4)
        self.assertFalse(info["is_integer"])


class TestFractionConversions(unittest.TestCase):
    """Test cases for fraction limit_denominator, ratio extraction, and GCD."""

    def test_limit_denominator_approximation(self) -> None:
        """Verify limit_denominator simplifies inexact float representations."""
        float_val = 0.142857142857
        approx = approximate_float_to_fraction(float_val, max_denominator=10)
        self.assertEqual(approx, Fraction(1, 7))

    def test_extract_integer_ratio(self) -> None:
        """Verify as_integer_ratio returns (numerator, denominator) tuple."""
        ratio = extract_integer_ratio(Fraction(3, 4))
        self.assertEqual(ratio, (3, 4))

    def test_convert_to_numeric_types(self) -> None:
        """Verify type conversion to float, int, and str."""
        converted = convert_fraction_to_numeric_types(Fraction(7, 3))
        self.assertAlmostEqual(converted["float_val"], 2.3333333333333335)
        self.assertEqual(converted["int_val"], 2)
        self.assertEqual(converted["str_val"], "7/3")

    def test_compute_fraction_gcd(self) -> None:
        """Verify GCD calculation between fraction numerators using math.gcd."""
        gcd_val = compute_fraction_gcd(Fraction(12, 5), Fraction(18, 5))
        self.assertEqual(gcd_val, 6)


class TestFractionArithmetic(unittest.TestCase):
    """Test cases for arithmetic operators, divmod, and relational comparisons."""

    def test_perform_fraction_arithmetic(self) -> None:
        """Verify addition, subtraction, multiplication, division, modulo, and exponentiation."""
        a = Fraction(2, 7)
        b = Fraction(1, 3)
        res = perform_fraction_arithmetic(a, b)
        self.assertEqual(res["addition"], Fraction(13, 21))
        self.assertEqual(res["subtraction"], Fraction(-1, 21))
        self.assertEqual(res["multiplication"], Fraction(2, 21))

    def test_calculate_divmod(self) -> None:
        """Verify divmod quotient (int) and remainder (Fraction)."""
        quot, rem = calculate_fraction_divmod(Fraction(7, 3), Fraction(2, 3))
        self.assertEqual(quot, 3)
        self.assertEqual(rem, Fraction(1, 3))

    def test_compare_fractions(self) -> None:
        """Verify relational comparison operators between fractions."""
        cmp_res = compare_fractions(Fraction(2, 7), Fraction(1, 3))
        self.assertFalse(cmp_res["equal"])
        self.assertTrue(cmp_res["less_than"])

    def test_mixed_type_arithmetic(self) -> None:
        """Verify return types when combining Fraction with int and float."""
        res = mixed_type_arithmetic(Fraction(1, 2), 2, 0.5)
        self.assertIsInstance(res["frac_plus_int"], Fraction)
        self.assertIsInstance(res["frac_plus_float"], float)


class TestFractionAdvancedMath(unittest.TestCase):
    """Test cases for rounding, summation, and Decimal interop."""

    def test_apply_rounding(self) -> None:
        """Verify floor, ceil, trunc, and round output values."""
        res = apply_rounding_and_truncation(Fraction(7, 3))
        self.assertEqual(res["floor"], 2)
        self.assertEqual(res["ceil"], 3)
        self.assertEqual(res["trunc"], 2)

    def test_accumulate_fractions(self) -> None:
        """Verify exact sum over a list of fractions."""
        fracs = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
        self.assertEqual(accumulate_fractions(fracs), Fraction(1, 1))

    def test_decimal_interop(self) -> None:
        """Verify exact Decimal to Fraction conversion and round-trip calculation."""
        res = decimal_fraction_conversion_interop(Decimal("0.125"))
        self.assertEqual(res["converted_fraction"], Fraction(1, 8))
        self.assertEqual(res["roundtrip_decimal"], Decimal("0.125"))


class TestFractionRangeEvolution(unittest.TestCase):
    """Test cases for fractional range generation, memory efficiency, and introspection."""

    def test_generate_fractional_range_positive_step(self) -> None:
        """Verify fractional range generation with positive step."""
        f_range = generate_fractional_range(Fraction(0, 1), Fraction(1, 1), Fraction(1, 4))
        expected = [Fraction(0, 1), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]
        self.assertEqual(f_range, expected)

    def test_generate_fractional_range_negative_step(self) -> None:
        """Verify fractional range generation with negative step."""
        f_range = generate_fractional_range(Fraction(1, 1), Fraction(0, 1), Fraction(-1, 4))
        expected = [Fraction(1, 1), Fraction(3, 4), Fraction(1, 2), Fraction(1, 4)]
        self.assertEqual(f_range, expected)

    def test_memory_efficiency(self) -> None:
        """Verify O(1) RAM footprint for range objects relative to list."""
        mem = compare_range_and_fraction_memory_efficiency(1000)
        self.assertTrue(mem["is_range_constant_memory"])

    def test_inspect_range(self) -> None:
        """Verify range attributes and methods introspection output."""
        range_info = inspect_range_attributes_and_methods()
        self.assertEqual(range_info["start"], 10)
        self.assertEqual(range_info["stop"], 100)
        self.assertEqual(range_info["step"], 5)

    def test_version_evolution(self) -> None:
        """Verify version evolution notes map all major milestones."""
        evo = document_python_version_evolution()
        self.assertIn("Python 3.12-3.13", evo)


if __name__ == "__main__":
    unittest.main()
