"""
Unittest Suite for Emulating Numeric Types Module (`emulating_numeric_types`)
"""
import unittest
from emulating_numeric_types.emulate_add import Vector2D as AddVector
from emulating_numeric_types.emulate_sub import Currency
from emulating_numeric_types.emulate_mul import Vector2D as MulVector
from emulating_numeric_types.emulate_matmul import Matrix2x2
from emulating_numeric_types.emulate_truediv import Vector2D as TrueDivVector
from emulating_numeric_types.emulate_floordiv import Vector2D as FloorDivVector
from emulating_numeric_types.emulate_mod import TimeOffset
from emulating_numeric_types.emulate_divmod import SmartQuantity
from emulating_numeric_types.emulate_pow import PowerBase
from emulating_numeric_types.emulate_bitwise_and import BitMask
from emulating_numeric_types.emulate_bitwise_or import BitFlags
from emulating_numeric_types.emulate_bitwise_xor import BitField
from emulating_numeric_types.emulate_shift import BitRegister
from emulating_numeric_types.emulate_unary import Point2D


class TestEmulatingNumericTypes(unittest.TestCase):
    """Test suite validating numeric type emulation dunder methods."""

    def test_addition(self) -> None:
        """Tests __add__, __radd__, __iadd__."""
        v1 = AddVector(3.0, 4.0)
        v2 = AddVector(1.0, 2.0)
        self.assertEqual(v1 + v2, AddVector(4.0, 6.0))
        self.assertEqual(10.0 + v1, AddVector(13.0, 14.0))

        v1 += v2
        self.assertEqual(v1, AddVector(4.0, 6.0))

    def test_subtraction(self) -> None:
        """Tests __sub__, __rsub__, __isub__."""
        c1 = Currency(100.0)
        c2 = Currency(30.0)
        self.assertEqual(c1 - c2, Currency(70.0))
        self.assertEqual(200.0 - c2, Currency(170.0))

        c1 -= c2
        self.assertEqual(c1, Currency(70.0))

    def test_multiplication(self) -> None:
        """Tests __mul__, __rmul__, __imul__."""
        v1 = MulVector(2.0, 3.0)
        v2 = MulVector(4.0, 5.0)
        self.assertEqual(v1 * 3, MulVector(6.0, 9.0))
        self.assertEqual(2.5 * v1, MulVector(5.0, 7.5))
        self.assertEqual(v1 * v2, 23.0)  # Dot product: 2*4 + 3*5 = 23

        v1 *= 4
        self.assertEqual(v1, MulVector(8.0, 12.0))

    def test_matrix_multiplication(self) -> None:
        """Tests __matmul__, __imatmul__ (@ operator)."""
        m1 = Matrix2x2(1, 2, 3, 4)
        m2 = Matrix2x2(2, 0, 1, 2)
        expected = Matrix2x2(4, 4, 10, 8)
        self.assertEqual(m1 @ m2, expected)

        m1 @= m2
        self.assertEqual(m1, expected)

    def test_division(self) -> None:
        """Tests true division and floor division."""
        tv = TrueDivVector(10.0, 20.0)
        self.assertEqual(tv / 2, TrueDivVector(5.0, 10.0))
        self.assertEqual(100.0 / tv, TrueDivVector(10.0, 5.0))

        fv = FloorDivVector(17.0, 25.0)
        self.assertEqual(fv // 4, FloorDivVector(4.0, 6.0))
        self.assertEqual(100.0 // fv, FloorDivVector(5.0, 4.0))

    def test_modulo_and_divmod(self) -> None:
        """Tests __mod__ and __divmod__."""
        t1 = TimeOffset(3665)
        t2 = TimeOffset(60)
        self.assertEqual(t1 % t2, TimeOffset(5))

        q1 = SmartQuantity(23)
        q2 = SmartQuantity(5)
        quot, rem = divmod(q1, q2)
        self.assertEqual((quot, rem), (SmartQuantity(4), SmartQuantity(3)))

    def test_exponentiation(self) -> None:
        """Tests __pow__, __rpow__, pow(a, b, m)."""
        b = PowerBase(3)
        self.assertEqual(b ** 4, PowerBase(81))
        self.assertEqual(pow(b, 4, 10), PowerBase(1))
        self.assertEqual(2 ** b, PowerBase(8))

    def test_bitwise_operations(self) -> None:
        """Tests bitwise AND, OR, XOR, shifts."""
        b1 = BitMask(12)
        b2 = BitMask(10)
        self.assertEqual(b1 & b2, BitMask(8))

        f1 = BitFlags(4)
        f2 = BitFlags(2)
        self.assertEqual(f1 | f2, BitFlags(6))

        field1 = BitField(12)
        field2 = BitField(10)
        self.assertEqual(field1 ^ field2, BitField(6))

        reg = BitRegister(1)
        self.assertEqual(reg << 3, BitRegister(8))
        self.assertEqual(BitRegister(8) >> 2, BitRegister(2))

    def test_unary_operators(self) -> None:
        """Tests __neg__, __pos__, __abs__, __invert__."""
        pt = Point2D(3.0, -4.0)
        self.assertEqual(-pt, Point2D(-3.0, 4.0))
        self.assertEqual(+pt, Point2D(3.0, -4.0))
        self.assertEqual(abs(pt), 5.0)  # hypot(3, 4) = 5
        self.assertEqual(~Point2D(5, 10), Point2D(-6, -11))


if __name__ == "__main__":
    unittest.main()
