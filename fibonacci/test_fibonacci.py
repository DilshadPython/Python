"""
Unittest Suite for Fibonacci & Algorithms Module (`fibonacci`)
"""
import unittest
from fibonacci.fibonacci_iterative import get_fibonacci_nth, generate_fibonacci_sequence
from fibonacci.fibonacci_recursive import fibonacci_recursive
from fibonacci.fibonacci_memoization import fibonacci_memoized, clear_cache, get_cache_size
from fibonacci.fibonacci_lru_cache import fibonacci_lru
from fibonacci.fibonacci_generator import fibonacci_generator
from fibonacci.fibonacci_iterator import FibonacciIterator
from fibonacci.fizzbuzz_algorithm import fizzbuzz_item, generate_fizzbuzz_sequence


class TestFibonacci(unittest.TestCase):
    """Test suite covering all Fibonacci implementations and FizzBuzz logic."""

    def test_fibonacci_iterative(self) -> None:
        """Tests iterative Fibonacci computation."""
        self.assertEqual(get_fibonacci_nth(0), 0)
        self.assertEqual(get_fibonacci_nth(1), 1)
        self.assertEqual(get_fibonacci_nth(10), 55)
        self.assertEqual(generate_fibonacci_sequence(6), [0, 1, 1, 2, 3, 5])

        with self.assertRaises(ValueError):
            get_fibonacci_nth(-1)

    def test_fibonacci_recursive(self) -> None:
        """Tests naive recursive Fibonacci computation."""
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_recursive(10), 55)

        with self.assertRaises(ValueError):
            fibonacci_recursive(-5)

    def test_fibonacci_memoized(self) -> None:
        """Tests explicit dictionary memoization."""
        clear_cache()
        self.assertEqual(fibonacci_memoized(10), 55)
        self.assertEqual(fibonacci_memoized(50), 12586269025)
        self.assertGreater(get_cache_size(), 10)

    def test_fibonacci_lru_cache(self) -> None:
        """Tests standard library @lru_cache decorator."""
        fibonacci_lru.cache_clear()
        self.assertEqual(fibonacci_lru(10), 55)
        self.assertEqual(fibonacci_lru(100), 354224848179261915075)
        info = fibonacci_lru.cache_info()
        self.assertGreater(info.hits + info.misses, 0)

    def test_fibonacci_generator(self) -> None:
        """Tests generator lazy evaluation."""
        gen = fibonacci_generator(6)
        results = list(gen)
        self.assertEqual(results, [0, 1, 1, 2, 3, 5])

    def test_fibonacci_iterator(self) -> None:
        """Tests custom object-oriented iterator class."""
        fib_iter = FibonacciIterator(6)
        results = list(fib_iter)
        self.assertEqual(results, [0, 1, 1, 2, 3, 5])

    def test_fizzbuzz_algorithm(self) -> None:
        """Tests FizzBuzz single item and sequence evaluation."""
        self.assertEqual(fizzbuzz_item(3), "Fizz")
        self.assertEqual(fizzbuzz_item(5), "Buzz")
        self.assertEqual(fizzbuzz_item(15), "FizzBuzz")
        self.assertEqual(fizzbuzz_item(7), "7")

        seq = generate_fizzbuzz_sequence(15)
        self.assertEqual(seq[2], "Fizz")      # index 2 corresponds to number 3
        self.assertEqual(seq[4], "Buzz")      # index 4 corresponds to number 5
        self.assertEqual(seq[14], "FizzBuzz")  # index 14 corresponds to number 15


if __name__ == "__main__":
    unittest.main()
