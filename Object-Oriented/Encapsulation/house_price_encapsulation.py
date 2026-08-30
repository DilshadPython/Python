"""House Price Encapsulation Demonstration Module.

This module demonstrates property getters and setters for managing house price encapsulation cleanly.
"""


class House:
    """Class encapsulating house pricing with validation."""

    def __init__(self, initial_price: float = 0.0) -> None:
        """Initialize House with an optional initial price."""
        self._price: float = float(initial_price)

    @property
    def price(self) -> float:
        """Property getter returning house price."""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Property setter validating house price is non-negative.

        Args:
            new_price: New price value.

        Raises:
            ValueError: If new_price is negative.
        """
        parsed_price = float(new_price)
        if parsed_price < 0:
            raise ValueError("House price cannot be negative.")
        self._price = parsed_price


if __name__ == "__main__":
    print("=== House Price Encapsulation Demonstration ===")
    h1 = House(745662)
    h2 = House(850434)

    print(f"House 1 Price: £{h1.price:,.2f}")
    print(f"House 2 Price: £{h2.price:,.2f}")

    h1.price = 444444
    print(f"House 1 Updated Price: £{h1.price:,.2f}")
