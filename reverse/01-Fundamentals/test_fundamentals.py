# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import unittest: Python standard library unit testing framework.
# - from reverse_sequence_basics import demonstrate_reversed_builtin, demonstrate_inplace_reverse
# - from reverse_slicing_conversions import demonstrate_slicing_reversal, demonstrate_reversal_type_errors
# =========================================================================
import unittest
from reverse_sequence_basics import demonstrate_reversed_builtin, demonstrate_inplace_reverse
from reverse_slicing_conversions import demonstrate_slicing_reversal, demonstrate_reversal_type_errors


class TestReverseFundamentals(unittest.TestCase):
    """
    Unit tests for Step 1 Fundamentals (reversed(), .reverse(), slicing, and exception handling).
    """

    def test_reversed_builtin(self) -> None:
        res = demonstrate_reversed_builtin([1, 2, 3], ("a", "b"), "hello")
        self.assertEqual(res["reversed_list"], [3, 2, 1])
        self.assertEqual(res["reversed_tuple"], ("b", "a"))
        self.assertEqual(res["reversed_str"], "olleh")

    def test_inplace_reverse(self) -> None:
        res = demonstrate_inplace_reverse([10, 20, 30])
        self.assertEqual(res["mutated_list"], [30, 20, 10])
        self.assertIsNone(res["method_return_value"])

    def test_slicing_reversal(self) -> None:
        res = demonstrate_slicing_reversal([1, 2, 3, 4], "Flask")
        self.assertEqual(res["full_sliced_list"], [4, 3, 2, 1])
        self.assertEqual(res["full_sliced_str"], "ksalF")
        self.assertEqual(res["stepped_sliced_list"], [4, 2])

    def test_reversal_type_errors(self) -> None:
        res = demonstrate_reversal_type_errors()
        self.assertTrue(res["set_type_error_caught"])
        self.assertTrue(res["int_type_error_caught"])


if __name__ == "__main__":
    unittest.main()
