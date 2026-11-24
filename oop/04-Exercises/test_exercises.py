"""
Unit test suite verifying Object-Oriented Exercises (03-Exercises).
"""
# "import module" loads unittest from standard library framework.
import unittest

# "from module import name" imports exercise classes into test scope.
from bank_account_exercise import BankAccount, SavingsAccount
from vehicle_fleet_exercise import ElectricCar, Vehicle


class TestOOPExercises(unittest.TestCase):
    """Test suite covering BankAccount, SavingsAccount, Vehicle, and ElectricCar exercises."""

    def test_bank_account_operations(self):
        """Verify BankAccount deposits, withdrawals, and insufficient funds guards."""
        acc = BankAccount("Alice", 500.0)
        self.assertEqual(acc.balance, 500.0)

        acc.deposit(200.0)
        self.assertEqual(acc.balance, 700.0)

        acc.withdraw(150.0)
        self.assertEqual(acc.balance, 550.0)

        with self.assertRaises(ValueError):
            acc.withdraw(1000.0)

    def test_savings_account_interest(self):
        """Verify SavingsAccount interest calculation and application."""
        sav = SavingsAccount("Bob", 1000.0, 0.05)
        sav.apply_interest()
        self.assertEqual(sav.balance, 1050.0)

    def test_vehicle_fleet(self):
        """Verify Vehicle mileage accumulation and ElectricCar battery charging."""
        v = Vehicle("Toyota", "Corolla", 2020)
        self.assertEqual(v.mileage, 0.0)

        v.drive(150.0)
        self.assertEqual(v.mileage, 150.0)
        self.assertIn("Toyota Corolla", v.vehicle_info())

        ev = ElectricCar("Tesla", "Model 3", 2023, 75.0)
        self.assertEqual(ev.battery_level_percent, 100.0)
        ev.drive(80.0)
        self.assertEqual(ev.mileage, 80.0)
        self.assertEqual(ev.charge(), 100.0)


if __name__ == "__main__":
    unittest.main()
