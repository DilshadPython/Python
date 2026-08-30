"""Vehicle Hierarchy Demonstration Module.

This module demonstrates a Vehicle base class and derived Car and Van subclasses.
"""


class Vehicle:
    """Base vehicle class managing registration, type, and fuel level."""

    def __init__(self, registration: str, vehicle_type: str, gas_capacity: float) -> None:
        """Initialize Vehicle instance."""
        self.registration: str = registration
        self.vehicle_type: str = vehicle_type
        self.gas_level: float = float(gas_capacity)
        self.max_speed_mph: float = 0.0

    def description(self) -> str:
        """Return formatted vehicle description string."""
        return f"Vehicle Reg: {self.registration}, Type: {self.vehicle_type}, Fuel: {self.gas_level}L"

    def fill_tank(self, liters: float = 120.0) -> None:
        """Refuel vehicle tank."""
        self.gas_level = float(liters)

    def set_max_speed(self, speed_mph: float) -> None:
        """Set vehicle maximum speed capability."""
        self.max_speed_mph = float(speed_mph)


class Car(Vehicle):
    """Car subclass inheriting from Vehicle."""

    pass


class Van(Vehicle):
    """Van subclass inheriting from Vehicle with tire count attribute."""

    def __init__(self, registration: str, vehicle_type: str, gas_capacity: float, tire_count: int = 4) -> None:
        """Initialize Van instance with tire count."""
        super().__init__(registration, vehicle_type, gas_capacity)
        self.tire_count: int = tire_count


if __name__ == "__main__":
    print("=== Vehicle Hierarchy Demonstration ===")
    car = Car("AM80 YTR", "Audi", 80.0)
    van = Van("RM69 GHT", "Ford Transit", 120.0, tire_count=6)

    car.set_max_speed(220)
    van.set_max_speed(120)

    print(car.description(), f"| Max Speed: {car.max_speed_mph} mph")
    print(van.description(), f"| Tires: {van.tire_count} | Max Speed: {van.max_speed_mph} mph")
