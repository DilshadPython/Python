"""
Unit test suite for Step 1: Fraction Fundamentals & Conversions.
"""
# "import unittest" loads standard unit testing framework.
import unittest
# "from fractions import Fraction" imports rational number class.
from fractions import Fraction
# "from decimal import Decimal" imports decimal arithmetic support.
from decimal import Decimal

# "from fraction_basics import ..." imports fundamental helper functions.
from fraction_basics import (
    create_fraction_from_integers,
    create_fraction_from_string,
    create_fraction_from_float_and_decimal,
    inspect_fraction_components,
)
# "from fraction_conversions import ..." imports conversion helper functions.
from fraction_conversions import (
    approximate_float_to_fraction,
    extract_integer_ratio,
    convert_fraction_to_numeric_types,
    compute_fraction_gcd,
)


class TestFractionFundamentals(unittest.TestCase):
    """
    Test suite verifying Fraction instantiation, reduction, inspection, and conversions.
    """

    def test_create_fraction_from_integers_simplification(self) -> None:
        """Verify automatic GCD reduction when creating fractions from integers."""
        f = create_fraction_from_integers(6, 9)
        self.assertEqual(f.numerator, 2)
        self.assertEqual(f.denominator, 3)
        self.assertEqual(str(f), "2/3")

    def test_create_fraction_from_zero_denominator_raises_exception(self) -> None:
        """Verify ZeroDivisionError is raised on zero denominator."""
        with self.assertRaises(ZeroDivisionError):
            create_fraction_from_integers(5, 0)

    def test_create_fraction_from_string_parsing(self) -> None:
        """Verify parsing fraction strings including whitespace and decimal strings."""
        f1 = create_fraction_from_string(" 5 / 10 ")
        self.assertEqual(f1, Fraction(1, 2))

        f2 = create_fraction_from_string("-1.25")
        self.assertEqual(f2, Fraction(-5, 4))

    def test_create_fraction_from_float_and_decimal(self) -> None:
        """Verify creating Fraction objects from float and Decimal."""
        f_float = create_fraction_from_float_and_decimal(0.5)
        self.assertEqual(f_float, Fraction(1, 2))

        dec = Decimal("0.75")
        f_dec = create_fraction_from_float_and_decimal(dec)
        self.assertEqual(f_dec, Fraction(3, 4))

    def test_inspect_fraction_components(self) -> None:
        """Verify numerator, denominator, and string component dictionary outputs."""
        f = Fraction(8, 12)
        info = inspect_fraction_components(f)
        self.assertEqual(info["numerator"], 2)
        self.assertEqual(info["denominator"], 3)
        self.assertEqual(info["str"], "2/3")
        self.assertFalse(info["is_integer"])

    def test_limit_denominator_approximation(self) -> None:
        """Verify limit_denominator simplifies inexact float representations."""
        pi_approx = 3.1415926535
        f_approx = approximate_float_to_fraction(pi_approx, max_denominator=10)
        self.assertEqual(f_approx, Fraction(22, 7))

    def test_extract_integer_ratio(self) -> None:
        """Verify as_integer_ratio returns (numerator, denominator) tuple."""
        f = Fraction(5, 8)
        num, den = extract_integer_ratio(f)
        self.assertEqual(num, 5)
        self.assertEqual(den, 8)

    def test_convert_fraction_to_numeric_types(self) -> None:
        """Verify type conversion to float, int, and str."""
        f = Fraction(7, 2)
        converted = convert_fraction_to_numeric_types(f)
        self.assertEqual(converted["float_val"], 3.5)
        self.assertEqual(converted["int_val"], 3)
        self.assertEqual(converted["str_val"], "7/2")

    def test_compute_fraction_gcd(self) -> None:
        """Verify GCD calculation between fraction numerators using math.gcd."""
        f1 = Fraction(12, 5)
        f2 = Fraction(18, 7)
        gcd_val = compute_fraction_gcd(f1, f2)
        self.assertEqual(gcd_val, 6)


if __name__ == "__main__":
    unittest.main()
