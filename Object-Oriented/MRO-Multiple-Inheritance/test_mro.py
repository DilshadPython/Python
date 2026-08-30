"""Unit Test Suite for MRO and Multiple Inheritance Module.

This module provides unittest coverage for MRO linearization and method execution order.
"""

import unittest
from multiple_inheritance_mro import DerivedD1, DerivedD2, get_mro_class_names


class TestMRO(unittest.TestCase):
    """Unit tests for MRO resolution and method inheritance."""

    def test_derived_d1_mro(self) -> None:
        """Verify DerivedD1 MRO order (SubB -> BaseA -> BaseC -> object)."""
        mro = get_mro_class_names(DerivedD1)
        self.assertEqual(mro, ["DerivedD1", "SubB", "BaseA", "BaseC", "object"])
        d1 = DerivedD1()
        self.assertEqual(d1.execute_action(), "Executed in BaseA")

    def test_derived_d2_diamond_mro(self) -> None:
        """Verify DerivedD2 diamond MRO order (SubB -> DiamondC -> BaseA -> object)."""
        mro = get_mro_class_names(DerivedD2)
        self.assertEqual(mro, ["DerivedD2", "SubB", "DiamondC", "BaseA", "object"])
        d2 = DerivedD2()
        self.assertEqual(d2.execute_action(), "Executed in DiamondC")


if __name__ == "__main__":
    unittest.main()
