"""
Comprehensive Unit Test Suite for Python Yield & Generator Modules.
Tests basic yield pattern generation, generator expressions, memory comparisons,
'yield from' sub-generator delegation, bidirectional .send()/.throw()/.close(),
range sequence integration, and dir() attribute reflection.
"""

# "import module" loads standard library modules into global namespace.
import os
import sys
import unittest
# "from module import name" imports specific class/function symbols directly into local scope.
from pathlib import Path

# Ensure module directory is in sys.path for direct imports
sys.path.insert(0, str(Path(__file__).parent))

# Import tutorial generator functions directly into test scope
from yield_basics import generate_pattern, generate_number_sequence, collect_generated_pattern
from yield_generator_expressions import compare_memory_footprint, filter_even_squares, aggregate_generator_sum
from yield_from_delegation import sub_generator, delegating_generator, flatten_nested
from yield_coroutine_send import running_accumulator, echo_with_error_handling


class TestYieldBasics(unittest.TestCase):
    """Test basic generator function yield mechanics and pattern generation."""

    def test_generate_pattern(self):
        patterns = list(generate_pattern(4))
        expected = ['', '#', '##', '###']
        self.assertEqual(patterns, expected)

    def test_generate_pattern_invalid(self):
        with self.assertRaises(ValueError):
            list(generate_pattern(-1))

    def test_generate_number_sequence(self):
        nums = list(generate_number_sequence(1, 10, 2))
        self.assertEqual(nums, [1, 3, 5, 7, 9])

    def test_generate_number_sequence_negative_step(self):
        nums = list(generate_number_sequence(10, 0, -2))
        self.assertEqual(nums, [10, 8, 6, 4, 2])

    def test_generate_number_sequence_zero_step(self):
        with self.assertRaises(ValueError):
            list(generate_number_sequence(0, 10, 0))

    def test_collect_generated_pattern(self):
        self.assertEqual(len(collect_generated_pattern(5)), 5)


class TestYieldGeneratorExpressions(unittest.TestCase):
    """Test generator expression evaluation, memory footprints, and pipeline aggregating."""

    def test_compare_memory_footprint(self):
        list_size, gen_size = compare_memory_footprint(50000)
        self.assertTrue(list_size > gen_size)
        self.assertTrue(gen_size < 1000)  # Generator object header size is constant and small

    def test_filter_even_squares(self):
        even_sqs = list(filter_even_squares(10))
        # Squares of 0..9: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81
        # Evens: 0, 4, 16, 36, 64
        self.assertEqual(even_sqs, [0, 4, 16, 36, 64])

    def test_aggregate_generator_sum(self):
        res = aggregate_generator_sum(10)  # 0, 3, 5, 6, 9 -> sum = 23
        self.assertEqual(res, 23)


class TestYieldFromDelegation(unittest.TestCase):
    """Test 'yield from' sub-generator delegation and recursive flattening."""

    def test_sub_generator(self):
        gen = sub_generator("Test", 2)
        self.assertEqual(next(gen), "Test-Item-1")
        self.assertEqual(next(gen), "Test-Item-2")
        with self.assertRaises(StopIteration) as ctx:
            next(gen)
        self.assertEqual(ctx.exception.value, "Completed Test")

    def test_delegating_generator(self):
        gen = delegating_generator()
        yielded_items = []
        try:
            while True:
                yielded_items.append(next(gen))
        except StopIteration as stop:
            returned_results = stop.value

        self.assertEqual(yielded_items, ["Alpha-Item-1", "Alpha-Item-2", "Alpha-Item-3", "Beta-Item-1", "Beta-Item-2"])
        self.assertEqual(returned_results, ["Completed Alpha", "Completed Beta"])

    def test_flatten_nested(self):
        nested = [1, [2, [3, 4], 5], 6]
        flattened = list(flatten_nested(nested))
        self.assertEqual(flattened, [1, 2, 3, 4, 5, 6])


class TestYieldCoroutineSend(unittest.TestCase):
    """Test bidirectional generator communication via .send(), .throw(), and .close()."""

    def test_running_accumulator(self):
        acc = running_accumulator(10.0)
        self.assertEqual(next(acc), 10.0)
        self.assertEqual(acc.send(5.0), 15.0)
        self.assertEqual(acc.send(2.5), 17.5)
        with self.assertRaises(StopIteration) as ctx:
            acc.send(None)
        self.assertEqual(ctx.exception.value, 17.5)

    def test_echo_with_error_handling(self):
        gen = echo_with_error_handling()
        self.assertEqual(next(gen), "Ready")
        res = gen.throw(ValueError("Simulated error"))
        self.assertEqual(res, "Caught error: Simulated error")


class TestYieldRangeAndReflectionIntegration(unittest.TestCase):
    """Test generator reflection matrix using dir() and range object integration."""

    def test_generator_dir_reflection(self):
        gen = generate_pattern(3)
        attributes = dir(gen)
        self.assertIn('gi_frame', attributes)
        self.assertIn('gi_running', attributes)
        self.assertIn('gi_code', attributes)
        self.assertIn('send', attributes)
        self.assertIn('throw', attributes)
        self.assertIn('close', attributes)

    def test_range_properties_and_dir(self):
        r = range(10, 100, 10)
        self.assertEqual(r.start, 10)
        self.assertEqual(r.stop, 100)
        self.assertEqual(r.step, 10)
        self.assertIn('start', dir(r))
        self.assertIn('stop', dir(r))
        self.assertIn('step', dir(r))
        self.assertTrue(50 in r)
        self.assertFalse(55 in r)


if __name__ == '__main__':
    unittest.main()
