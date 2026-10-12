"""
Unit test suite for Step 2: Advanced Reversal Protocols & Containers.
"""
# "import unittest" loads unit testing framework.
import unittest

# "from custom_reversed_protocol import ..." imports protocol classes and functions.
from custom_reversed_protocol import (
    CustomReversibleContainer,
    SequenceFallbackContainer,
    demonstrate_custom_reversed_protocol,
    demonstrate_sequence_fallback_protocol,
)
# "from iterator_reversal_helpers import ..." imports container reversal functions.
from iterator_reversal_helpers import (
    reverse_dictionary_views,
    reverse_deque_in_place,
    reverse_tuple_sequence,
    reverse_generator_or_set,
)


class TestReversalProtocols(unittest.TestCase):
    """
    Test suite verifying __reversed__() protocol hook, sequence fallback, dict view reversal, and deques.
    """

    def test_demonstrate_custom_reversed_protocol(self) -> None:
        """Verify custom __reversed__() method execution."""
        sample = [1, 2, 3, 4]
        res = demonstrate_custom_reversed_protocol(sample)
        self.assertEqual(res, [4, 3, 2, 1])

    def test_demonstrate_sequence_fallback_protocol(self) -> None:
        """Verify sequence fallback using __len__() and __getitem__() for reversed()."""
        sample = ["a", "b", "c"]
        res = demonstrate_sequence_fallback_protocol(sample)
        self.assertEqual(res, ["c", "b", "a"])

    def test_reverse_dictionary_views(self) -> None:
        """Verify dict_keys, dict_values, and dict_items view reversal (Python 3.8+)."""
        d = {"first": 10, "second": 20, "third": 30}
        views = reverse_dictionary_views(d)

        self.assertEqual(views["reversed_keys"], ["third", "second", "first"])
        self.assertEqual(views["reversed_values"], [30, 20, 10])
        self.assertEqual(views["reversed_items"], [("third", 30), ("second", 20), ("first", 10)])

    def test_reverse_deque_in_place(self) -> None:
        """Verify collections.deque.reverse() in-place operation."""
        elems = [10, 20, 30]
        res = reverse_deque_in_place(elems)
        self.assertEqual(res, [30, 20, 10])

    def test_reverse_tuple_sequence(self) -> None:
        """Verify tuple extended slicing reversal [::-1]."""
        tpl = (1, 2, 3)
        self.assertEqual(reverse_tuple_sequence(tpl), (3, 2, 1))

    def test_reverse_generator_or_set(self) -> None:
        """Verify set / generator materialization before reversing."""
        gen = (x * 2 for x in range(3))  # 0, 2, 4
        res = reverse_generator_or_set(gen)
        self.assertEqual(res, [4, 2, 0])


if __name__ == "__main__":
    unittest.main()
