"""Unit tests for the decorator tutorial module.

Verifies wrapper execution, time measurement decorators, return value preservation,
and metadata retention using functools.wraps.
"""

import unittest

from decorator.calculate_time import time_you_need, walking_to_work
from decorator.collect_time import collect_time, sample_task
from decorator.deco import go_to_work
from decorator.make_chocolate import make_chocolate, new_chocolate
from decorator.make_coffe import make_coffee, new_coffee
from decorator.make_tea import make_tea, new_tea


class TestDecoratorTutorial(unittest.TestCase):
    """Test suite covering Python decorator behaviors and utilities."""

    def test_calculate_time_preserves_metadata_and_return_value(self):
        """Verify @time_you_need retains docstring and returns wrapped function output."""
        self.assertEqual(walking_to_work.__name__, "walking_to_work")
        self.assertIn("Simulate walking", walking_to_work.__doc__)
        result = walking_to_work("Library", delay=0.01)
        self.assertEqual(result, "Arrived at Library")

    def test_collect_time_decorator(self):
        """Verify @collect_time decorator preserves function output."""
        result = sample_task(duration=0.01)
        self.assertEqual(result, "Task completed")

    def test_manual_timing_go_to_work(self):
        """Verify manual timer function returns elapsed float > 0."""
        elapsed = go_to_work(walk_duration=0.01)
        self.assertIsInstance(elapsed, float)
        self.assertGreater(elapsed, 0.0)

    def test_beverage_decorators_return_values(self):
        """Verify tea, coffee, and chocolate decorators return their expected strings."""
        choc_result = new_chocolate("Dark Chocolate", time_needed=0.01)
        self.assertIn("Dark Chocolate is ready!", choc_result)

        coffee_result = new_coffee("Espresso", time_needed=0.01)
        self.assertEqual(coffee_result, "Espresso brewed successfully.")

        tea_result = new_tea("Green Tea", time_needed=0.01)
        self.assertIn("Green Tea ready by", tea_result)

    def test_custom_decorator_closure(self):
        """Verify standard closure structure and call count tracking."""
        calls = []

        def track(fn):
            def wrapper(*args, **kwargs):
                calls.append(fn.__name__)
                return fn(*args, **kwargs)
            return wrapper

        @track
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(calls, ["add"])


if __name__ == "__main__":
    unittest.main()
