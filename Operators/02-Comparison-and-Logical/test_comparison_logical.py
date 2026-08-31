"""
Unit test suite for Step 2: Comparison, Identity, Logical, & Bitwise Operators.
"""
# "import module" loads unittest framework.
import unittest

# "from module import name" imports comparison and logical functions into test scope.
from comparison_operators import (
    evaluate_comparison_operators,
    evaluate_identity_operators,
    evaluate_membership_operators,
)
from logical_bitwise_operators import (
    demonstrate_bitwise_operators,
    demonstrate_logical_operators,
    demonstrate_short_circuit_evaluation,
)


class TestComparisonAndLogicalOperators(unittest.TestCase):
    """Test suite covering relational comparisons, identity checks, membership, and bitwise logic."""

    def test_relational_comparisons(self):
        """Verify comparison operators ==, !=, >, <, >=, <=."""
        eq, ne, gt, lt, ge, le = evaluate_comparison_operators(15.0, 10.0)
        self.assertFalse(eq)
        self.assertTrue(ne)
        self.assertTrue(gt)
        self.assertFalse(lt)
        self.assertTrue(ge)
        self.assertFalse(le)

    def test_identity_operators(self):
        """Verify identity operators (is, is not) distinguish alias vs distinct objects."""
        list_a = [1, 2, 3]
        list_b = list_a          # Alias pointing to same memory address
        list_c = [1, 2, 3]       # Distinct instance with equal contents

        is_alias, is_same, is_not_same = evaluate_identity_operators(list_a, list_b, list_c)
        self.assertTrue(is_alias)
        self.assertFalse(is_same)
        self.assertTrue(is_not_same)
        self.assertEqual(list_a, list_c)  # Contents equal, but identity distinct

    def test_membership_operators(self):
        """Verify membership operators (in, not in)."""
        fruits = ["apple", "banana", "cherry"]
        is_present, is_absent = evaluate_membership_operators("banana", fruits)
        self.assertTrue(is_present)
        self.assertFalse(is_absent)

        _, is_durian_absent = evaluate_membership_operators("durian", fruits)
        self.assertTrue(is_durian_absent)

    def test_logical_operators(self):
        """Verify logical boolean operations (and, or, not)."""
        and_res, or_res, not_a, not_b = demonstrate_logical_operators(True, False)
        self.assertFalse(and_res)
        self.assertTrue(or_res)
        self.assertFalse(not_a)
        self.assertTrue(not_b)

    def test_short_circuit_evaluation(self):
        """Verify short-circuit OR skips evaluating second operand if first is True."""
        tracker = {}
        result = demonstrate_short_circuit_evaluation(tracker, trigger_second=True)
        self.assertTrue(result)
        self.assertTrue(tracker.get("first_func_called"))
        self.assertNotIn("second_func_called", tracker)

    def test_bitwise_operators(self):
        """Verify bitwise operations AND, OR, XOR, NOT, Shift Left, Shift Right."""
        bit_and, bit_or, bit_xor, bit_not, shift_l, shift_r = demonstrate_bitwise_operators(0b1100, 0b1010)
        self.assertEqual(bit_and, 0b1000)  # 12 & 10 = 8
        self.assertEqual(bit_or, 0b1110)   # 12 | 10 = 14
        self.assertEqual(bit_xor, 0b0110)  # 12 ^ 10 = 6
        self.assertEqual(bit_not, -13)     # ~12 = -13
        self.assertEqual(shift_l, 48)      # 12 << 2 = 48
        self.assertEqual(shift_r, 5)       # 10 >> 1 = 5


if __name__ == "__main__":
    unittest.main()
