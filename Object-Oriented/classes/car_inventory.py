"""Car Inventory Demonstration Module.

This module demonstrates class attributes (`profit_margin`, `total_cars_in_store`),
instance counter tracking, and price calculation methods.
"""


class Car:
    """Class representing a car in store inventory."""

    profit_margin: float = 1.09
    total_cars_in_store: int = 0

    def __init__(self, make: str, year: int, color: str, model_type: str, price: float) -> None:
        """Initialize Car instance and increment store inventory counter."""
        self.make: str = make
        self.year: int = year
        self.color: str = color
        self.model_type: str = model_type
        self.price: float = float(price)

        Car.total_cars_in_store += 1

    def get_details(self) -> str:
        """Return formatted car details string."""
        return f"{self.make} {self.model_type} ({self.year}) - {self.color} - ${self.price:,.2f}"

    def calculate_price_with_profit(self) -> float:
        """Calculate and return price after applying profit margin."""
        return self.price * Car.profit_margin

    def apply_profit(self) -> None:
        """Update price in-place with profit margin."""
        self.price = self.calculate_price_with_profit()


if __name__ == "__main__":
    print("=== Car Inventory Demonstration ===")
    car1 = Car("Audi", 2017, "Black", "S3", 33000.0)
    car2 = Car("BMW", 2016, "Gray", "Z3", 28500.0)

    print("Car 1 Details:", car1.get_details())
    print("Car 1 Price with Profit:", car1.calculate_price_with_profit())
    print("Total Cars in Store:", Car.total_cars_in_store)
