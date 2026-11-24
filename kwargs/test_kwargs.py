"""Unit tests for the kwargs module tutorial functions.

Validates the behavior of *args, **kwargs, default parameters, and edge cases.
"""

import unittest

from kwargs.alcohols import drinks_type as drinks_catalog
from kwargs.ava_score import average_score, avarage_score
from kwargs.clients_plus_args import register_client
from kwargs.customer_kwargs import register_customer
from kwargs.drink_type import drinks_type
from kwargs.students import register_student


class TestKwargsTutorial(unittest.TestCase):
    """Test suite covering functions with *args and **kwargs."""

    def test_average_score_calculations(self):
        """Test arithmetic mean calculation with variable argument counts."""
        self.assertAlmostEqual(average_score(66, 74, 85, 89), 78.5)
        self.assertAlmostEqual(average_score(10, 20, 30), 20.0)
        self.assertEqual(average_score(100), 100.0)
        self.assertEqual(average_score(), 0.0)
        # Test backward-compatible alias
        self.assertEqual(avarage_score(50, 50), 50.0)

    def test_register_client_with_extras(self):
        """Test combining mandatory arguments with *extras tuple."""
        client = register_client("Alice", 25, "London", "VIP")
        self.assertEqual(client["name"], "Alice")
        self.assertEqual(client["age"], 25)
        self.assertEqual(client["extras"], ["London", "VIP"])

        # No extras
        basic_client = register_client("Bob", 30)
        self.assertEqual(basic_client["extras"], [])

    def test_register_customer_combined(self):
        """Test flexible customer registration with *args and **kwargs."""
        result = register_customer("Alice", 28, city="Berlin", email="alice@test.com")
        self.assertEqual(result["args"], ["Alice", 28])
        self.assertEqual(result["kwargs"], {"city": "Berlin", "email": "alice@test.com"})

    def test_drinks_type_required_and_kwargs(self):
        """Test required positional parameters with **kwargs."""
        drink = drinks_type("Whisky", 25.99, brand="Jack Daniels", in_stock=True)
        self.assertEqual(drink["name"], "Whisky")
        self.assertEqual(drink["price"], 25.99)
        self.assertEqual(drink["details"]["brand"], "Jack Daniels")
        self.assertTrue(drink["details"]["in_stock"])

    def test_drinks_catalog(self):
        """Test drinks catalog with *names and **details."""
        catalog = drinks_catalog("Gin", "Vodka", country="UK", rating=5)
        self.assertEqual(catalog["names"], ["Gin", "Vodka"])
        self.assertEqual(catalog["details"]["rating"], 5)

    def test_register_student(self):
        """Test student profile generation with default arguments."""
        student = register_student("Sam", "German")
        self.assertEqual(student["student_name"], "Sam")
        self.assertEqual(student["level"], "Beginner")

        advanced = register_student("Emma", "Japanese", level="N1")
        self.assertEqual(advanced["level"], "N1")


if __name__ == "__main__":
    unittest.main()
