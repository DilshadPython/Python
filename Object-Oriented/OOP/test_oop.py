"""Unit Test Suite for OOP Module.

This module provides unittest coverage for pet hierarchy, vehicle hierarchy, and point geometry.
"""

import unittest
from pet_hierarchy import Dog, Cat
from vehicle_hierarchy import Vehicle, Car, Van
from point_geometry import Point


class TestOOP(unittest.TestCase):
    """Unit tests for OOP module components."""

    def test_pet_hierarchy(self) -> None:
        """Verify Dog and Cat inheritance and sound emission."""
        dog = Dog("Raffi", 8, "white", "male")
        cat = Cat("Mimi", 2, "black", "female")
        self.assertEqual(dog.speak(), "Bark!")
        self.assertEqual(cat.speak(), "Meow!")

    def test_vehicle_hierarchy(self) -> None:
        """Verify Vehicle, Car, and Van hierarchy."""
        car = Car("AM80 YTR", "Audi", 80.0)
        van = Van("RM69 GHT", "Ford Transit", 120.0, tire_count=6)
        self.assertEqual(car.gas_level, 80.0)
        self.assertEqual(van.tire_count, 6)

    def test_point_geometry(self) -> None:
        """Verify Point vector addition, subtraction, dot product, and magnitude."""
        p1 = Point(3, 4)
        p2 = Point(1, 2)

        p_add = p1 + p2
        self.assertEqual(p_add.coordinates, (4.0, 6.0))

        p_sub = p1 - p2
        self.assertEqual(p_sub.coordinates, (2.0, 2.0))

        dot_prod = p1 * p2
        self.assertEqual(dot_prod, 11.0)  # (3*1) + (4*2) = 11

        self.assertEqual(abs(p1), 5.0)  # sqrt(3^2 + 4^2) = 5.0


if __name__ == "__main__":
    unittest.main()
