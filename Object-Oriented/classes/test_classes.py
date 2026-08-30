"""Unit Test Suite for Classes Module.

This module provides unittest coverage for UserAccount and Car inventory functionality.
"""

import unittest
from user_account import UserAccount
from car_inventory import Car


class TestClasses(unittest.TestCase):
    """Unit tests for user account and car inventory classes."""

    def test_user_account(self) -> None:
        """Verify UserAccount full name string formatting."""
        user = UserAccount("John", "Doe")
        self.assertEqual(user.get_full_name(), "John Doe")

    def test_car_inventory(self) -> None:
        """Verify Car initialization, profit margin, and store counter."""
        initial_store_count = Car.total_cars_in_store
        car = Car("Audi", 2017, "Black", "S3", 30000.0)

        self.assertEqual(Car.total_cars_in_store, initial_store_count + 1)
        self.assertAlmostEqual(car.calculate_price_with_profit(), 32700.0, places=2)


if __name__ == "__main__":
    unittest.main()
