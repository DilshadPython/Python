# =========================================================================
# UNIT TESTS: PYTHON OBJECT-ORIENTED PROGRAMMING (OOP)
# Standardized test suite for cloud_app/tutorials/oop_basics.py
# =========================================================================
import unittest
from cloud_app.tutorials.oop_basics import (
    User,
    CompanyEmployee,
    DataReflectionModel,
    Vehicle,
    BankAccountSecure,
    Animal,
    Mammal,
    Dog,
    SmartPhone,
    PDFReport,
    CarComposition,
    CustomContainer,
    TemperatureConverter,
    UserFactory,
    BaseDatabaseConnector,
    PostgresConnector,
    LoggingDict,
    OneBasedList,
    BoundedIntegerDescriptor,
    JSONSerializerMixin,
    PluginBase,
    AnalyticsPlugin,
    BankAccount,
    SavingsAccount,
    FleetVehicle,
    ElectricCarFleet,
    demonstrate_class_definition_basics,
    demonstrate_class_and_instance_attributes,
    demonstrate_class_and_instance_data,
    demonstrate_constructors_and_initialization,
    demonstrate_encapsulation_and_properties,
    demonstrate_inheritance_and_super,
    demonstrate_multiple_inheritance_and_mro,
    demonstrate_polymorphism_and_duck_typing,
    demonstrate_composition_vs_inheritance,
    demonstrate_magic_dunder_methods,
    demonstrate_static_and_class_methods,
    demonstrate_abstract_base_classes,
    demonstrate_builtin_subclassing,
    demonstrate_mixins_and_descriptors,
    demonstrate_bank_account_exercise,
    demonstrate_vehicle_fleet_exercise,
)


class TestOopTutorial(unittest.TestCase):
    """Unit test suite verifying Object-Oriented Programming (OOP) tutorial functions."""

    def test_class_definition_basics(self) -> None:
        res = demonstrate_class_definition_basics()
        self.assertEqual(res["user_full_name"], "Alice Smith")
        self.assertEqual(res["user_email"], "alice.smith@company.com")
        self.assertEqual(res["discounted_payment"], 225.0)
        self.assertTrue(res["is_user_instance"])

        with self.assertRaises(ValueError):
            User("", "Smith", 100.0)

        with self.assertRaises(ValueError):
            User("Alice", "Smith", -50.0)

    def test_class_and_instance_attributes(self) -> None:
        res = demonstrate_class_and_instance_attributes()
        self.assertGreaterEqual(res["total_employees"], 2)
        self.assertEqual(res["emp1_company"], "TechCorp Solutions")
        self.assertEqual(res["emp2_company_shadow"], "TechCorp Labs")
        self.assertTrue(res["has_tag_before"])
        self.assertFalse(res["has_tag_after"])

        with self.assertRaises(TypeError):
            CompanyEmployee(123, "Invalid", 50000.0)  # type: ignore

    def test_class_and_instance_data(self) -> None:
        res = demonstrate_class_and_instance_data()
        self.assertGreaterEqual(res["total_instances_created"], 2)
        self.assertEqual(res["data_version"], "v2.4")
        self.assertEqual(res["note_before"], "Priority Processing")
        self.assertFalse(res["has_note_after"])
        self.assertIn("inspect_public_attributes", res["public_attrs"])

    def test_constructors_and_initialization(self) -> None:
        res = demonstrate_constructors_and_initialization()
        self.assertEqual(res["vehicle_str"], "2022 Toyota Corolla")
        self.assertEqual(res["initial_odometer"], 15000.0)
        self.assertEqual(res["updated_odometer"], 15250.5)

        with self.assertRaises(ValueError):
            Vehicle("Ford", "Focus", 1800)  # Invalid year < 1886

    def test_encapsulation_and_properties(self) -> None:
        res = demonstrate_encapsulation_and_properties()
        self.assertEqual(res["owner"], "John Doe")
        self.assertEqual(res["initial_balance"], 500.0)
        self.assertEqual(res["updated_balance"], 1200.50)
        self.assertEqual(res["mangled_key"], "_BankAccountSecure__balance")
        self.assertEqual(res["mangled_value"], 1200.50)
        self.assertEqual(res["reset_balance"], 0.0)

        acc = BankAccountSecure("Test", 100.0)
        with self.assertRaises(ValueError):
            acc.balance = -50.0

    def test_inheritance_and_super(self) -> None:
        res = demonstrate_inheritance_and_super()
        self.assertEqual(res["dog_name"], "Buddy")
        self.assertEqual(res["breed"], "Golden Retriever")
        self.assertTrue(res["is_animal_instance"])
        self.assertTrue(res["is_mammal_instance"])
        self.assertIn("Buddy (Golden Retriever)", res["sound_output"])

    def test_multiple_inheritance_and_mro(self) -> None:
        res = demonstrate_multiple_inheritance_and_mro()
        self.assertIn("SmartPhone Booting", res["boot_sequence"])
        self.assertEqual(
            res["mro_chain"],
            ["SmartPhone", "Camera", "Phone", "Device", "object"],
        )

    def test_polymorphism_and_duck_typing(self) -> None:
        res = demonstrate_polymorphism_and_duck_typing()
        self.assertEqual(res["total_rendered"], 3)
        self.assertIn("PDF Document", res["pdf_output"])
        self.assertIn("HTML Document", res["html_output"])

    def test_composition_vs_inheritance(self) -> None:
        res = demonstrate_composition_vs_inheritance()
        self.assertEqual(res["car_model"], "Mustang")
        self.assertEqual(res["engine_hp"], 450)
        self.assertIn("450 HP", res["start_status"])

    def test_magic_dunder_methods(self) -> None:
        res = demonstrate_magic_dunder_methods()
        self.assertEqual(res["c1_str"], "Container 'Alpha' with 2 items")
        self.assertEqual(res["c3_len"], 4)
        self.assertEqual(res["c3_first_item"], 10)
        self.assertTrue(res["containers_equal"])

    def test_static_and_class_methods(self) -> None:
        res = demonstrate_static_and_class_methods()
        self.assertEqual(res["boiling_point_f"], 212.0)
        self.assertEqual(res["converted_list_f"], [32.0, 77.0, 212.0])
        self.assertEqual(res["user1_email"], "bob.miller@company.com")
        self.assertEqual(res["user2_full_name"], "Jane Doe")

        u = UserFactory.from_formatted_string("John-Doe-100")
        self.assertEqual(u.payment, 100.0)

    def test_abstract_base_classes(self) -> None:
        res = demonstrate_abstract_base_classes()
        self.assertTrue(res["cannot_instantiate_abstract"])
        self.assertTrue(res["is_connector_subclass"])
        self.assertIn("PostgreSQL", res["conn_status"])

    def test_builtin_subclassing(self) -> None:
        res = demonstrate_builtin_subclassing()
        self.assertIn("user_id", res["log_dict_keys"])
        self.assertEqual(res["log_history_count"], 2)
        self.assertEqual(res["one_list_first_item"], "Python")
        self.assertEqual(res["one_list_second_item"], "OOP")
        self.assertEqual(res["updated_first_item"], "Modern Python")

        one_l = OneBasedList([10, 20])
        with self.assertRaises(IndexError):
            _ = one_l[0]

    def test_mixins_and_descriptors(self) -> None:
        res = demonstrate_mixins_and_descriptors()
        self.assertEqual(res["plugin_id"], "PLG-101")
        self.assertEqual(res["score"], 95)
        self.assertTrue(res["invalid_bound_raised"])
        self.assertIn("AnalyticsPlugin", res["registered_plugin_names"])
        self.assertIn('"score": 95', res["json_output"])

    def test_bank_account_exercise(self) -> None:
        res = demonstrate_bank_account_exercise()
        self.assertEqual(res["account_holder"], "Robert Johnson")
        self.assertEqual(res["balance_after_deposit"], 1500.0)
        self.assertEqual(res["balance_after_withdrawal"], 1300.0)
        self.assertEqual(res["balance_after_interest"], 1365.0)

        sa = SavingsAccount("Test", 100.0, 0.10)
        with self.assertRaises(ValueError):
            sa.withdraw(500.0)  # Insufficient funds

    def test_vehicle_fleet_exercise(self) -> None:
        res = demonstrate_vehicle_fleet_exercise()
        self.assertEqual(res["mileage_after_trip"], 150.0)
        self.assertEqual(res["recharged_level"], 100.0)
        self.assertEqual(res["battery_capacity"], 75.0)
        self.assertIn("Tesla Model Y", res["initial_info"])


if __name__ == "__main__":
    unittest.main()
