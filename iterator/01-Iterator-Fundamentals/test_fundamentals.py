"""
Unit test suite for Step 1: Iterator Protocol Basics & Container Iterators.
"""
# "import unittest" loads standard unit testing framework.
import unittest
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path

# "from iterator_protocol_basics import ..." imports protocol verification functions.
from iterator_protocol_basics import (
    verify_iterable_and_iterator,
    manual_iteration_with_stop_iteration,
    fetch_next_with_default,
)
# "from container_iterators import ..." imports container iterator functions.
from container_iterators import (
    iterate_dictionary_views,
    iterate_file_lines,
    iterate_tuples_and_strings,
)


class TestIteratorFundamentals(unittest.TestCase):
    """
    Test suite verifying Iterable vs Iterator types, StopIteration handling, and container iterators.
    """

    def test_verify_iterable_and_iterator(self) -> None:
        """Verify list is iterable but not iterator, while iter(list) is both."""
        data = [1, 2, 3]
        is_iter_data, is_iterator_data = verify_iterable_and_iterator(data)
        self.assertTrue(is_iter_data)
        self.assertFalse(is_iterator_data)

        itr = iter(data)
        is_iter_itr, is_iterator_itr = verify_iterable_and_iterator(itr)
        self.assertTrue(is_iter_itr)
        self.assertTrue(is_iterator_itr)

    def test_manual_iteration_with_stop_iteration(self) -> None:
        """Verify manual try-except StopIteration loop collects all items."""
        sample = ["Paris", "London", "Berlin"]
        collected = manual_iteration_with_stop_iteration(sample)
        self.assertEqual(collected, sample)

    def test_fetch_next_with_default(self) -> None:
        """Verify next(iterator, default) returns items and handles exhaustion cleanly."""
        sample = ["Audi", "Volvo"]
        fetched = fetch_next_with_default(sample, 4, default_value="EMPTY")
        self.assertEqual(fetched, ["Audi", "Volvo", "EMPTY", "EMPTY"])

    def test_iterate_dictionary_views(self) -> None:
        """Verify dict key, value, and item view iterators."""
        d = {"a": 10, "b": 20}
        views = iterate_dictionary_views(d)
        self.assertEqual(views["keys"], ["a", "b"])
        self.assertEqual(views["values"], [10, 20])
        self.assertEqual(views["items"], [("a", 10), ("b", 20)])

    def test_iterate_tuples_and_strings(self) -> None:
        """Verify str_iterator and tuple_iterator."""
        res = iterate_tuples_and_strings("ABC", (1, 2))
        self.assertEqual(res["chars"], ["A", "B", "C"])
        self.assertEqual(res["tuple_elements"], [1, 2])

    def test_iterate_file_lines(self) -> None:
        """Verify file line iteration on grade.txt."""
        grade_file = Path(__file__).parent.parent / "grade.txt"
        if grade_file.exists():
            lines = iterate_file_lines(grade_file)
            self.assertGreater(len(lines), 0)


if __name__ == "__main__":
    unittest.main()
