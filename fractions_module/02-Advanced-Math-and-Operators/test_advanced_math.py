"""
Unit test suite for Step 2: Fraction Arithmetic, Comparison, & Advanced Math.
"""
# "import unittest" loads unit testing framework.
import unittest
# "from fractions import Fraction" imports rational number class.
from fractions import Fraction
# "from decimal import Decimal" imports decimal arithmetic support.
from decimal import Decimal

# "from fraction_arithmetic_ops import ..." imports arithmetic functions.
from fraction_arithmetic_ops import (
    perform_fraction_arithmetic,
    calculate_fraction_divmod,
    compare_fractions,
    mixed_type_arithmetic,
)
# "from fraction_advanced_math import ..." imports math integration functions.
from fraction_advanced_math import (
    apply_rounding_and_truncation,
    accumulate_fractions,
    decimal_fraction_conversion_interop,
)


class TestFractionAdvancedMath(unittest.TestCase):
    """
    Test suite verifying fraction arithmetic, comparisons, mixed-type coercion, and rounding.
    """

    def test_perform_fraction_arithmetic(self) -> None:
        """Verify addition, subtraction, multiplication, division, modulo, and exponentiation."""
        a = Fraction(2, 7)
        b = Fraction(1, 3)
        results = perform_fraction_arithmetic(a, b)

        self.assertEqual(results["addition"], Fraction(13, 21))
        self.assertEqual(results["subtraction"], Fraction(-1, 21))
        self.assertEqual(results["multiplication"], Fraction(2, 21))
        self.assertEqual(results["division"], Fraction(6, 7))
        self.assertEqual(results["floor_division"], 0)
        self.assertEqual(results["modulo"], Fraction(2, 7))
        self.assertEqual(results["exponentiation"], Fraction(4, 49))

    def test_calculate_fraction_divmod(self) -> None:
        """Verify divmod quotient (int) and remainder (Fraction)."""
        a = Fraction(7, 2)  # 3.5
        b = Fraction(4, 3)  # 1.3333...
        quotient, remainder = calculate_fraction_divmod(a, b)
        self.assertEqual(quotient, 2)
        self.assertEqual(remainder, Fraction(5, 6))
        self.assertEqual(quotient * b + remainder, a)

    def test_compare_fractions(self) -> None:
        """Verify relational comparison operators between fractions."""
        a = Fraction(1, 2)
        b = Fraction(2, 4)
        c = Fraction(3, 4)

        comp_equal = compare_fractions(a, b)
        self.assertTrue(comp_equal["equal"])
        self.assertFalse(comp_equal["not_equal"])

        comp_unequal = compare_fractions(a, c)
        self.assertTrue(comp_unequal["less_than"])
        self.assertTrue(comp_unequal["less_equal"])
        self.assertFalse(comp_unequal["greater_than"])

    def test_mixed_type_arithmetic(self) -> None:
        """Verify type return values when combining Fraction with int and float."""
        frac = Fraction(3, 4)
        res = mixed_type_arithmetic(frac, 2, 0.5)

        self.assertIsInstance(res["frac_plus_int"], Fraction)
        self.assertEqual(res["frac_plus_int"], Fraction(11, 4))

        self.assertIsInstance(res["frac_plus_float"], float)
        self.assertEqual(res["frac_plus_float"], 1.25)

    def test_apply_rounding_and_truncation(self) -> None:
        """Verify floor, ceil, trunc, and round output values for positive and negative fractions."""
        f_pos = Fraction(7, 3)  # 2.333...
        res_pos = apply_rounding_and_truncation(f_pos)
        self.assertEqual(res_pos["floor"], 2)
        self.assertEqual(res_pos["ceil"], 3)
        self.assertEqual(res_pos["trunc"], 2)

        f_neg = Fraction(-7, 3)  # -2.333...
        res_neg = apply_rounding_and_truncation(f_neg)
        self.assertEqual(res_neg["floor"], -3)
        self.assertEqual(res_neg["ceil"], -2)
        self.assertEqual(res_neg["trunc"], -2)

    def test_accumulate_fractions(self) -> None:
        """Verify exact sum over a list of fractions."""
        fractions = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
        total = accumulate_fractions(fractions)
        self.assertEqual(total, Fraction(1, 1))

    def test_decimal_fraction_conversion_interop(self) -> None:
        """Verify exact Decimal to Fraction conversion and round-trip calculation."""
        dec = Decimal("0.375")
        res = decimal_fraction_conversion_interop(dec)
        self.assertEqual(res["converted_fraction"], Fraction(3, 8))
        self.assertEqual(res["roundtrip_decimal"], dec)


if __name__ == "__main__":
    unittest.main()
