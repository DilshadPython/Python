"""
Unit test suite for Step 2: Custom Class Iterators & Sentinel Iterators.
"""
# "import unittest" loads standard unit testing framework.
import unittest

# "from custom_class_iterator import ..." imports custom iterator classes and helper functions.
from custom_class_iterator import (
    AlphabetIterator,
    BoundedFibonacciIterator,
    collect_alphabet_sequence,
    collect_fibonacci_sequence,
)
# "from infinite_and_sentinel_iter import ..." imports sentinel iterator functions.
from infinite_and_sentinel_iter import (
    CounterCallable,
    iterate_until_sentinel,
    simulate_file_sentinel_reading,
)


class TestCustomIterators(unittest.TestCase):
    """
    Test suite verifying AlphabetIterator, BoundedFibonacciIterator, and two-argument iter(callable, sentinel).
    """

    def test_alphabet_iterator_limit(self) -> None:
        """Verify AlphabetIterator yields requested character count and raises StopIteration."""
        alphabet = collect_alphabet_sequence(4)
        self.assertEqual(alphabet, ["A", "B", "C", "D"])

        itr = AlphabetIterator(char_limit=2)
        self.assertEqual(next(itr), "A")
        self.assertEqual(next(itr), "B")
        with self.assertRaises(StopIteration):
            next(itr)

    def test_bounded_fibonacci_iterator(self) -> None:
        """Verify BoundedFibonacciIterator generates Fibonacci numbers up to max bound."""
        fibs = collect_fibonacci_sequence(20)
        self.assertEqual(fibs, [0, 1, 1, 2, 3, 5, 8, 13])

    def test_iterate_until_sentinel(self) -> None:
        """Verify two-argument iter(callable, sentinel) stops when sentinel value is met."""
        counter = CounterCallable(start=10)
        values = iterate_until_sentinel(counter, sentinel_value=14)
        self.assertEqual(values, [10, 11, 12, 13])

    def test_simulate_file_sentinel_reading(self) -> None:
        """Verify sentinel file line reading stops on empty string sentinel."""
        stream = ["Line 1", "Line 2", ""]
        read_data = simulate_file_sentinel_reading(stream)
        self.assertEqual(read_data, ["Line 1", "Line 2"])


if __name__ == "__main__":
    unittest.main()
