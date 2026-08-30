"""Unit Test Suite for Abstract Base Classes Module.

This module provides unittest coverage for abstract base class instantiation enforcement,
subclass concrete implementations, type validation, and history tracking.
"""

import unittest
from abstract_base_class import GetterSetter, ValueContainer
from abstract_inheritance import GetSetParent, GetSetInt, GetSetList


class TestAbstractBaseClass(unittest.TestCase):
    """Unit tests for Abstract Base Class behavior and instantiation enforcement."""

    def test_abc_instantiation_raises_typeerror(self) -> None:
        """Verify instantiating an abstract class with abstractmethods raises TypeError."""
        with self.assertRaises(TypeError):
            GetterSetter()  # type: ignore

        with self.assertRaises(TypeError):
            GetSetParent()  # type: ignore

    def test_value_container_implementation(self) -> None:
        """Verify ValueContainer concrete subclass implementation of GetterSetter."""
        container = ValueContainer(10)
        self.assertEqual(container.get_val(), 10)
        container.set_val(50)
        self.assertEqual(container.get_val(), 50)

    def test_get_set_int_validation(self) -> None:
        """Verify GetSetInt restricts stored values strictly to integers."""
        gsi = GetSetInt(100)
        gsi.set_val(42)
        self.assertEqual(gsi.get_val(), 42)
        
        # Passing non-integer defaults to 0
        gsi.set_val("not_an_int")
        self.assertEqual(gsi.get_val(), 0)

    def test_get_set_list_history(self) -> None:
        """Verify GetSetList records value history and returns recent value."""
        gsl = GetSetList(1)
        gsl.set_val(5)
        gsl.set_val(10)
        self.assertEqual(gsl.get_val(), 10)
        self.assertEqual(gsl.get_vals(), [1, 5, 10])
        self.assertIn("3 values", gsl.show_docs())


if __name__ == "__main__":
    unittest.main()
