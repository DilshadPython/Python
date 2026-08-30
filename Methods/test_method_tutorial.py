# =========================================================================
# UNIT TESTS: PYTHON METHODS & OBJECT ARCHITECTURE
# Standardized test suite for method_basics.py
# =========================================================================
import unittest
from cloud_app.tutorials.method_basics import (
    BankAccount,
    UserProfile,
    StudentGrade,
    Vector2D,
    ProductInventory,
    demonstrate_instance_methods,
    demonstrate_class_and_static_methods,
    demonstrate_property_methods,
    demonstrate_special_dunder_methods,
    demonstrate_descriptor_protocol,
    inspect_object_methods,
)


class TestMethodTutorial(unittest.TestCase):
    """Test suite verifying all Python method types and object mechanics."""

    def test_instance_methods(self) -> None:
        res = demonstrate_instance_methods("alex_dev", 100.0)
        self.assertEqual(res["account_holder"], "alex_dev")
        self.assertEqual(res["balance_after_deposit"], 250.0)
        self.assertEqual(res["balance_after_withdraw"], 200.0)
        self.assertEqual(res["statement"]["total_transactions"], 3)

        # Test defensive exceptions
        account = BankAccount("test", 50.0)
        with self.assertRaises(TypeError):
            BankAccount(123, 50.0)  # type: ignore
        with self.assertRaises(ValueError):
            account.withdraw(1000.0)  # Insufficient funds

    def test_class_and_static_methods(self) -> None:
        res = demonstrate_class_and_static_methods("john_doe, admin")
        self.assertEqual(res["created_username"], "john_doe")
        self.assertEqual(res["created_role"], "admin")
        self.assertTrue(res["is_username_valid"])
        self.assertGreaterEqual(res["system_stats"]["total_users"], 1)

        # Test static method directly
        self.assertTrue(UserProfile.validate_username("valid_user99"))
        self.assertFalse(UserProfile.validate_username("ab"))  # Too short

    def test_property_methods(self) -> None:
        res = demonstrate_property_methods("Alex", 78.0)
        self.assertEqual(res["initial_letter"], "C")
        self.assertEqual(res["updated_score"], 92.5)
        self.assertEqual(res["updated_letter"], "A")
        self.assertEqual(res["reset_score"], 0.0)
        self.assertEqual(res["reset_letter"], "F")

        # Test property setter validation
        student = StudentGrade("Sam", 85.0)
        with self.assertRaises(ValueError):
            student.score = 150.0  # Out of range

    def test_special_dunder_methods(self) -> None:
        res = demonstrate_special_dunder_methods(3.0, 4.0)
        self.assertEqual(res["v1_str"], "Vector2D(3.0, 4.0)")
        self.assertEqual(res["v1_repr"], "Vector2D(x=3.0, y=4.0)")
        self.assertEqual(res["v3_added_str"], "Vector2D(6.0, 8.0)")
        self.assertTrue(res["vectors_equal"])
        self.assertEqual(res["v1_len"], 2)
        self.assertEqual(res["v1_callable_scaled"], 10.0)

    def test_descriptor_protocol(self) -> None:
        res = demonstrate_descriptor_protocol("Laptop", 5.0, 999.99)
        self.assertEqual(res["product_name"], "Laptop")
        self.assertEqual(res["initial_total"], 4999.95)
        self.assertEqual(res["updated_total"], 14999.85)

        # Test descriptor validation exception
        item = ProductInventory("Phone", 2.0, 499.99)
        with self.assertRaises(ValueError):
            item.quantity = -5.0  # Non-negative descriptor failure

    def test_inspect_object_methods(self) -> None:
        account = BankAccount("inspector", 100.0)
        res = inspect_object_methods(account)
        self.assertEqual(res["object_type"], "BankAccount")
        self.assertTrue(res["is_bank_account"])
        self.assertIn("deposit", res["sample_methods"])
        self.assertIn("withdraw", res["sample_methods"])

        with self.assertRaises(TypeError):
            inspect_object_methods(None)


if __name__ == "__main__":
    unittest.main()
