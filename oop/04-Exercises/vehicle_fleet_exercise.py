"""
Object-Oriented Programming Exercises: Vehicle Fleet Management.

This module provides an OOP exercise modeling a transport fleet with base class Vehicle
and derived subclasses Car and ElectricCar.
"""
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import List


class Vehicle:
    """Base class for transport fleet vehicles."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Initialize Vehicle attributes."""
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self._mileage: float = 0.0

    @property
    def mileage(self) -> float:
        """Getter property exposing total vehicle mileage."""
        return self._mileage

    def drive(self, distance: float) -> float:
        """Drive vehicle and accumulate mileage."""
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        self._mileage += distance
        return self._mileage

    def vehicle_info(self) -> str:
        """Return formatted vehicle details."""
        return f"{self.year} {self.make} {self.model} (Mileage: {self._mileage} km)"


class ElectricCar(Vehicle):
    """Subclass representing an electric car with battery capacity management."""

    def __init__(self, make: str, model: str, year: int, battery_capacity_kwh: float) -> None:
        """Initialize ElectricCar with battery capacity."""
        super().__init__(make, model, year)
        self.battery_capacity_kwh: float = battery_capacity_kwh
        self.battery_level_percent: float = 100.0

    def charge(self) -> float:
        """Fully charge vehicle battery to 100%."""
        self.battery_level_percent = 100.0
        return self.battery_level_percent
