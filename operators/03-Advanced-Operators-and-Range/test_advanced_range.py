"""
Unit test suite for Step 3: Special Operators & Range Evolution.
"""
# "import module" loads unittest framework.
import unittest

# "from module import name" imports operator getters and range evolution functions into test scope.
from range_operator_evolution import (
    compare_range_memory_efficiency,
    demonstrate_range_operator_features,
    inspect_range_attributes,
)
from walrus_and_special_operators import ItemRecord, calculate_discounted_price, sort_records_using_operator_getters
from dunder_operator_overloading_and_bitwise_flags import PermissionFlags


class TestAdvancedOperatorsAndRange(unittest.TestCase):
    """Test suite covering operator getters, parameter boundary operators, and range evolution."""

    def test_operator_getters_sorting(self):
        """Verify operator.attrgetter and operator.itemgetter sorting behavior."""
        items = [
            ItemRecord("Widget", 25.0, 4),
            ItemRecord("Gadget", 10.0, 10),
            ItemRecord("Gizmo", 50.0, 1),
        ]
        sorted_by_price, sorted_dicts = sort_records_using_operator_getters(items)

        self.assertEqual(sorted_by_price[0].name, "Gadget")
        self.assertEqual(sorted_by_price[-1].name, "Gizmo")

        self.assertEqual(sorted_dicts[0]["name"], "Widget")  # Total value 100.0 is highest

    def test_positional_and_keyword_only_operators(self):
        """Verify positional-only (/) and keyword-only (*) parameter syntax."""
        price = calculate_discounted_price(100.0, 0.20, tax_rate=0.10)
        self.assertEqual(price, 88.0)  # 100 * 0.80 * 1.10 = 88.0

        with self.assertRaises(ValueError):
            calculate_discounted_price(-10.0, 0.10)

    def test_range_attribute_inspection(self):
        """Verify dir(range) attribute inspection returns start, stop, step, count, index."""
        attrs = inspect_range_attributes()
        self.assertIn("start", attrs)
        self.assertIn("stop", attrs)
        self.assertIn("step", attrs)
        self.assertIn("count", attrs)
        self.assertIn("index", attrs)

    def test_range_operator_features(self):
        """Verify range attributes, containment, indexing, and count."""
        start, stop, step, contains_45, indexed_item, count_30 = demonstrate_range_operator_features()
        self.assertEqual(start, 10)
        self.assertEqual(stop, 100)
        self.assertEqual(step, 5)
        self.assertTrue(contains_45)
        self.assertEqual(indexed_item, 30)
        self.assertEqual(count_30, 1)

    def test_range_memory_efficiency(self):
        """Verify range O(1) RAM footprint relative to materialized list sample."""
        range_bytes, list_bytes = compare_range_memory_efficiency()
        self.assertLess(range_bytes, list_bytes)

    def test_custom_permission_flags_dunder_operators(self):
        """Verify Bitwise OR (|), AND (&), and Membership (in) dunder overloading."""
        read = PermissionFlags(PermissionFlags.READ)
        write = PermissionFlags(PermissionFlags.WRITE)
        exec_flag = PermissionFlags(PermissionFlags.EXEC)

        read_write = read | write
        self.assertTrue(PermissionFlags.READ in read_write)
        self.assertTrue(PermissionFlags.WRITE in read_write)
        self.assertFalse(PermissionFlags.EXEC in read_write)

        all_perms = read_write | exec_flag
        self.assertEqual(all_perms, PermissionFlags(0b111))


if __name__ == "__main__":
    unittest.main()
