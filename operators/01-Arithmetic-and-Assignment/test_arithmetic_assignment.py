"""
Unit test suite for Step 1: Arithmetic & Assignment Operators.
"""
# "import module" loads unittest framework.
import unittest

# "from module import name" imports arithmetic and assignment functions into test scope.
from arithmetic_operators import Matrix2D, basic_arithmetic_operations, operator_module_equivalents
from assignment_operators import (
    demonstrate_augmented_arithmetic_assignment,
    demonstrate_augmented_bitwise_assignment,
    demonstrate_walrus_assignment_expression,
)
from advanced_arithmetic_and_assignment_examples import (
    calculate_complex_arithmetic,
    demonstrate_inplace_sequence_mutations,
)


class TestArithmeticAndAssignmentOperators(unittest.TestCase):
    """Test suite covering arithmetic, matrix multiplication, and augmented assignment operators."""

    def test_basic_arithmetic(self):
        """Verify basic arithmetic operations +, -, *, /, //, %, **."""
        add, sub, mul, div, floordiv, mod, pow_val = basic_arithmetic_operations(10, 3)
        self.assertEqual(add, 13.0)
        self.assertEqual(sub, 7.0)
        self.assertEqual(mul, 30.0)
        self.assertAlmostEqual(div, 3.3333333333, places=5)
        self.assertEqual(floordiv, 3)
        self.assertEqual(mod, 1.0)
        self.assertEqual(pow_val, 1000.0)

    def test_zero_division_guard(self):
        """Verify ValueError is raised on division or modulo by zero."""
        with self.assertRaises(ValueError):
            basic_arithmetic_operations(10, 0)

    def test_operator_module_equivalents(self):
        """Verify operator module standard library calls."""
        add, mul, floordiv = operator_module_equivalents(8, 2)
        self.assertEqual(add, 10)
        self.assertEqual(mul, 16)
        self.assertEqual(floordiv, 4)

    def test_matrix_multiplication_operator(self):
        """Verify @ matrix multiplication operator over __matmul__ hook."""
        m1 = Matrix2D([[1, 2], [3, 4]])
        m2 = Matrix2D([[5, 6], [7, 8]])
        result = m1 @ m2
        expected = Matrix2D([[19.0, 22.0], [43.0, 50.0]])
        self.assertEqual(result, expected)

    def test_augmented_arithmetic_assignment(self):
        """Verify augmented arithmetic assignment calculations."""
        history = demonstrate_augmented_arithmetic_assignment(10.0)
        self.assertEqual(history["add_5"], 15.0)
        self.assertEqual(history["sub_3"], 12.0)
        self.assertEqual(history["mul_4"], 48.0)
        self.assertEqual(history["div_2"], 24.0)

    def test_augmented_bitwise_assignment(self):
        """Verify bitwise augmented assignment operations."""
        history = demonstrate_augmented_bitwise_assignment(16)
        self.assertEqual(history["initial"], 16)
        self.assertIn("shift_left_2", history)

    def test_walrus_assignment_expression(self):
        """Verify Walrus Operator := inline assignment."""
        words = ["apple", "cat", "elephant", "dog", "banana"]
        long_words, count = demonstrate_walrus_assignment_expression(words)
        self.assertEqual(long_words, ["APPLE", "ELEPHANT", "BANANA"])
        self.assertEqual(count, 3)

    def test_complex_arithmetic_operations(self):
        """Verify complex number arithmetic calculations."""
        res = calculate_complex_arithmetic(3 + 4j, 1 - 2j)
        self.assertEqual(res["addition"], 4 + 2j)
        self.assertEqual(res["subtraction"], 2 + 6j)
        self.assertEqual(res["multiplication"], 11 - 2j)

    def test_inplace_sequence_mutations(self):
        """Verify augmented assignment on list and set containers."""
        mutated_list, mutated_set = demonstrate_inplace_sequence_mutations()
        self.assertEqual(len(mutated_list), 10)
        self.assertEqual(mutated_list[:5], [1, 2, 3, 4, 5])
        self.assertEqual(mutated_set, {20, 30, 40})


if __name__ == "__main__":
    unittest.main()
