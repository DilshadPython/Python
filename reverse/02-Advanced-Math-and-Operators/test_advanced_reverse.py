# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import unittest: Python standard library testing framework.
# - from custom_reversible_class import CountdownSequence, LegacySequence, demonstrate_custom_reversible_objects
# - from matrix_and_dict_reverse import demonstrate_dictionary_reversing, demonstrate_matrix_reversing
# =========================================================================
import unittest
from custom_reversible_class import CountdownSequence, LegacySequence, demonstrate_custom_reversible_objects
from matrix_and_dict_reverse import demonstrate_dictionary_reversing, demonstrate_matrix_reversing


class TestAdvancedReverse(unittest.TestCase):
    """
    Unit tests for Step 2 Advanced (custom __reversed__, fallback sequence protocol, dict & matrix reversal).
    """

    def test_custom_reversible_class(self) -> None:
        cd = CountdownSequence(1, 3)
        self.assertEqual(list(cd), [1, 2, 3])
        self.assertEqual(list(reversed(cd)), [30, 20, 10])

    def test_legacy_sequence_fallback(self) -> None:
        leg = LegacySequence([10, 20, 30])
        self.assertEqual(list(reversed(leg)), [30, 20, 10])

    def test_demonstrate_custom_reversible_objects(self) -> None:
        res = demonstrate_custom_reversible_objects()
        self.assertEqual(res["forward_countdown"], [1, 2, 3, 4, 5])
        self.assertEqual(res["custom_reversed_countdown"], [50, 40, 30, 20, 10])
        self.assertEqual(res["fallback_reversed_legacy"], ["gamma", "beta", "alpha"])

    def test_dictionary_reversing(self) -> None:
        res = demonstrate_dictionary_reversing({"x": 10, "y": 20})
        self.assertEqual(res["reversed_keys"], ["y", "x"])
        self.assertEqual(res["reversed_values"], [20, 10])
        self.assertEqual(res["reversed_items"], [("y", 20), ("x", 10)])
        self.assertEqual(list(res["reversed_ordered_dict"].keys()), ["y", "x"])

    def test_matrix_reversing(self) -> None:
        m = [[1, 2], [3, 4]]
        res = demonstrate_matrix_reversing(m)
        self.assertEqual(res["row_reversed_matrix"], [[3, 4], [1, 2]])
        self.assertEqual(res["col_reversed_matrix"], [[2, 1], [4, 3]])
        self.assertEqual(res["rotated_180_matrix"], [[4, 3], [2, 1]])


if __name__ == "__main__":
    unittest.main()
