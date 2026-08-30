"""Polymorphic Animals Demonstration Module.

This module demonstrates polymorphism in Python: multiple distinct classes (`Dog`, `Cat`)
providing different implementations of a common interface method (`show_affection()`).
"""

from typing import List


class Animal:
    """Base class for all animals."""

    def __init__(self, name: str) -> None:
        """Initialize Animal with name."""
        self.name: str = name

    def eat(self, food: str) -> str:
        """Return string indicating animal eating food."""
        return f"{self.name} is eating {food}."

    def show_affection(self) -> str:
        """Base affection method (to be overridden by subclasses)."""
        return f"{self.name} shows affection."


class Dog(Animal):
    """Dog subclass implementing dog affection (wagging tail)."""

    def fetch(self, thing: str) -> str:
        """Return fetch action string."""
        return f"{self.name} goes after the {thing}."

    def show_affection(self) -> str:
        """Overridden method returning dog affection."""
        return f"{self.name} wags tail."


class Cat(Animal):
    """Cat subclass implementing cat affection (purring)."""

    def swat_string(self) -> str:
        """Return string swatting action."""
        return f"{self.name} shreds the string!"

    def show_affection(self) -> str:
        """Overridden method returning cat affection."""
        return f"{self.name} purrs."


def express_all_affections(animals: List[Animal]) -> List[str]:
    """Iterate polymorphically over animal instances and invoke show_affection().

    Args:
        animals: List of Animal objects.

    Returns:
        List of affection messages.
    """
    return [animal.show_affection() for animal in animals]


if __name__ == "__main__":
    print("=== Polymorphic Animals Demonstration ===")
    pets: List[Animal] = [Dog("Raffi"), Cat("Smikey"), Cat("Ali"), Dog("Tilly")]

    for msg in express_all_affections(pets):
        print(f"  {msg}")
