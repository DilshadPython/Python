"""
Unit Test Suite for Attributes & Methods across Developer Tiers (Beginner, Intermediate, Senior).

This module verifies:
1. `AttributeMethodInspector` engine categorization and resolution path generation.
2. Beginner level instance attributes, methods, `__str__`, and `__len__` (`beginner_attributes_methods.py`).
3. Intermediate `@classmethod`, `@staticmethod`, `@property` setters, and dynamic reflection (`intermediate_attributes_methods.py`).
4. Senior custom Data Descriptors, `__slots__` memory optimization, `__getattr__` fallback, and `__call__` callable objects (`senior_attributes_methods.py`).
"""

from pathlib import Path
import sys
import unittest

# Support both package and local directory import paths
root = Path(__file__).parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from attribute_method_inspector import AttributeMethodInspector
from beginner_attributes_methods import Book
from intermediate_attributes_methods import Account
from senior_attributes_methods import ValidatedStringDescriptor, MemoryOptimizedUser, DynamicAttributeInterceptors, CallableCalculator


class TestAttributesAndMethods(unittest.TestCase):
    """Test suite verifying attributes, methods, descriptors, and introspection."""

    def test_attribute_method_inspector(self) -> None:
        """Verify inspector categorizes attributes, methods, properties, and dunders correctly."""
        report = AttributeMethodInspector.inspect_object(Book("Test", "Author", 100))
        self.assertIn("title", report["instance_attributes"])
        self.assertIn("get_summary", report["public_methods"])
        self.assertIn("__str__", report["dunder_methods"])

        steps = AttributeMethodInspector.get_lookup_hierarchy(Book, "title")
        self.assertEqual(len(steps), 6)

    def test_beginner_attributes_methods(self) -> None:
        """Verify beginner Book instance attributes, methods, __str__, and __len__."""
        b = Book("Clean Code", "Robert Martin", 464)
        self.assertEqual(b.title, "Clean Code")
        self.assertEqual(b.author, "Robert Martin")
        self.assertEqual(b.get_summary(), "'Clean Code' by Robert Martin (464 pages)")
        self.assertEqual(str(b), "Book: Clean Code")
        self.assertEqual(len(b), 464)

    def test_intermediate_attributes_methods(self) -> None:
        """Verify intermediate Account property setter, classmethod, and staticmethod."""
        self.assertTrue(Account.validate_account_name("Alice"))
        self.assertFalse(Account.validate_account_name("  "))

        acc = Account.create_corporate_account("Acme Inc")
        self.assertEqual(acc.balance, 10000.0)

        acc.balance = 15000.0
        self.assertEqual(acc.balance, 15000.0)

        with self.assertRaises(ValueError):
            acc.balance = -500.0

    def test_senior_attributes_methods(self) -> None:
        """Verify senior descriptors, __slots__, __getattr__, and __call__."""

        class Profile:
            username = ValidatedStringDescriptor(min_length=3)

        p = Profile()
        p.username = "Monika"
        self.assertEqual(p.username, "Monika")

        with self.assertRaises(TypeError):
            p.username = 123  # type: ignore

        with self.assertRaises(ValueError):
            p.username = "ab"

        # __slots__ test
        mem_user = MemoryOptimizedUser(1, "test@domain.com")
        self.assertEqual(mem_user.user_id, 1)
        self.assertFalse(hasattr(mem_user, "__dict__"))

        # __getattr__ dynamic fallback
        dyn = DynamicAttributeInterceptors()
        self.assertEqual(dyn.known_attr, "Standard Value")
        self.assertIn("Dynamic Fallback", dyn.non_existent_prop)

        # __call__ test
        calc = CallableCalculator(multiplier=3)
        self.assertEqual(calc(10), 30)


if __name__ == "__main__":
    unittest.main()
