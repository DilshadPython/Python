"""Unit Test Suite for Class and Instance Data Module.

This module provides unittest coverage for class reflection, __delattr__ overrides,
and instance counting.
"""

import unittest
from class_reflection_and_dir import Person, inspect_all_dunder_attributes
from custom_attribute_deleter import TrackedProduct
from instance_counter import TrackedCar


class TestClassAndInstanceData(unittest.TestCase):
    """Unit tests for reflection, delattr interception, and instance tracking."""

    def test_person_reflection(self) -> None:
        """Verify person object reflection dictionary."""
        p = Person("Tomas")
        self.assertEqual(str(p), "Tomas")
        dunders = inspect_all_dunder_attributes(p)
        self.assertIn("Tomas", dunders["__dict__"])

    def test_tracked_product_delattr(self) -> None:
        """Verify __delattr__ interception on TrackedProduct."""
        prod = TrackedProduct("Laptop")
        self.assertEqual(prod.name, "Laptop")
        del prod.name
        with self.assertRaises(AttributeError):
            _ = prod.name

    def test_tracked_car_counter(self) -> None:
        """Verify TrackedCar shared instance count incrementing."""
        initial = TrackedCar.get_instance_count()
        c1 = TrackedCar(101)
        c2 = TrackedCar(102)
        self.assertEqual(TrackedCar.get_instance_count(), initial + 2)


if __name__ == "__main__":
    unittest.main()
