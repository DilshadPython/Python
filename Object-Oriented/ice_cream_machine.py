"""Ice Cream Machine Demonstration Module.

This module demonstrates component combination and domain modeling in Python OOP.
It models an IceCreamMachine that pairs ingredients (e.g. vanilla, chocolate) with toppings
(e.g. chocolate sauce, caramel).
"""

# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import List, Tuple


class IceCreamMachine:
    """Class representing an Ice Cream Machine combining ingredients and toppings."""

    def __init__(self, ingredients: List[str], toppings: List[str]) -> None:
        """Initialize IceCreamMachine with available ingredients and toppings lists.

        Args:
            ingredients: List of ice cream flavor strings.
            toppings: List of topping strings.
        """
        self.ingredients: List[str] = ingredients
        self.toppings: List[str] = toppings

    def generate_scoops(self) -> List[Tuple[str, str]]:
        """Generate all combinations of (ingredient, topping) pairs.

        Returns:
            List of tuples pairing each flavor with each topping.
        """
        scoop_combinations = []
        for flavor in self.ingredients:
            for topping in self.toppings:
                scoop_combinations.append((flavor, topping))
        return scoop_combinations

    def get_summary(self) -> str:
        """Return formatted summary of available combinations.

        Returns:
            Formatted summary string.
        """
        combos = self.generate_scoops()
        return f"Ingredients: {self.ingredients} | Toppings: {self.toppings} | Combinations: {combos}"


if __name__ == "__main__":
    print("=== Ice Cream Machine Demonstration ===")
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce", "caramel"])
    print(machine.get_summary())
    print("\nGenerated Scoop Pairs:")
    for pair in machine.generate_scoops():
        print("  - Flavor:", pair[0], "| Topping:", pair[1])
