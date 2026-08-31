"""
Unit test suite for Step 1: String & List Sequence Reversal Basics.
"""
# "import unittest" loads standard unit testing framework.
import unittest

# "from string_reversal import ..." imports string reversal functions.
from string_reversal import (
    reverse_string_by_slicing,
    reverse_string_with_builtin_reversed,
    reverse_word_order_in_sentence,
    compare_string_reversal_methods,
)
# "from list_in_place_reversal import ..." imports list reversal functions.
from list_in_place_reversal import (
    reverse_list_in_place,
    reverse_list_out_of_place,
    iterate_list_reversed,
    compare_list_reversal_side_effects,
)


class TestReversalBasics(unittest.TestCase):
    """
    Test suite verifying string reversal techniques and list in-place/out-of-place mechanics.
    """

    def test_reverse_string_by_slicing(self) -> None:
        """Verify extended slice [::-1] string reversal."""
        self.assertEqual(reverse_string_by_slicing("Python"), "nohtyP")
        self.assertEqual(reverse_string_by_slicing(""), "")
        self.assertEqual(reverse_string_by_slicing("A"), "A")

    def test_reverse_string_with_builtin_reversed(self) -> None:
        """Verify built-in reversed() + join() character reversal."""
        self.assertEqual(reverse_string_with_builtin_reversed("Hello World"), "dlroW olleH")

    def test_reverse_word_order_in_sentence(self) -> None:
        """Verify word order reversal in a sentence."""
        sentence = "On a Mac keyboard hitting Option"
        expected = "Option hitting keyboard Mac a On"
        self.assertEqual(reverse_word_order_in_sentence(sentence), expected)

    def test_compare_string_reversal_methods(self) -> None:
        """Verify comparison output dictionary for string reversal functions."""
        text = "abc def"
        comp = compare_string_reversal_methods(text)
        self.assertEqual(comp["slice_reversed"], "fed cba")
        self.assertEqual(comp["iterator_reversed"], "fed cba")
        self.assertEqual(comp["words_reversed"], "def abc")

    def test_reverse_list_in_place(self) -> None:
        """Verify list.reverse() mutates list in-place and returns None."""
        data = [1, 2, 3, 4]
        ret = reverse_list_in_place(data)
        self.assertIsNone(ret)
        self.assertEqual(data, [4, 3, 2, 1])

    def test_reverse_list_out_of_place(self) -> None:
        """Verify list[::-1] returns a new reversed list copy without mutating original."""
        original = [1, 2, 3]
        reversed_copy = reverse_list_out_of_place(original)
        self.assertEqual(reversed_copy, [3, 2, 1])
        self.assertEqual(original, [1, 2, 3])
        self.assertIsNot(reversed_copy, original)

    def test_iterate_list_reversed(self) -> None:
        """Verify list(reversed(data)) produces correct reversed list."""
        data = ["apple", "banana", "cherry"]
        self.assertEqual(iterate_list_reversed(data), ["cherry", "banana", "apple"])

    def test_compare_list_reversal_side_effects(self) -> None:
        """Verify list reversal side effect dictionary properties."""
        sample = [5, 10, 15]
        side_effects = compare_list_reversal_side_effects(sample)
        self.assertIsNone(side_effects["in_place_return_value"])
        self.assertEqual(side_effects["in_place_mutated"], [15, 10, 5])
        self.assertFalse(side_effects["is_same_object_slice"])


if __name__ == "__main__":
    unittest.main()
