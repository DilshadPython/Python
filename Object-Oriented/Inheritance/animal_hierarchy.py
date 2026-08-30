"""Animal Inheritance Hierarchy Module.

This module demonstrates single inheritance, method overriding, and type checking
using `isinstance()` and `issubclass()`.
"""


class Animal:
    """Base class for all animals."""

    def can_fly(self) -> bool:
        """Return whether animal can fly (default False)."""
        return False

    def can_speak(self) -> bool:
        """Return whether animal can speak (default False)."""
        return False


class Cat(Animal):
    """Cat subclass inheriting from Animal."""

    def __init__(self) -> None:
        """Initialize Cat instance."""
        self.number_of_feet: int = 4
        self.can_run: bool = True

    def can_fly(self) -> bool:
        """Cats cannot fly."""
        return False


class Pigeon(Animal):
    """Pigeon subclass inheriting from Animal."""

    def __init__(self) -> None:
        """Initialize Pigeon instance."""
        self.number_of_feet: int = 2
        self.can_run: bool = True

    def can_fly(self) -> bool:
        """Pigeons can fly."""
        return True


if __name__ == "__main__":
    print("=== Animal Inheritance Demonstration ===")
    my_cat = Cat()
    my_pigeon = Pigeon()

    print("Cat Can Fly?:", my_cat.can_fly())
    print("Pigeon Can Fly?:", my_pigeon.can_fly())

    print("isinstance(my_cat, Animal):", isinstance(my_cat, Animal))
    print("issubclass(Cat, Animal):", issubclass(Cat, Animal))
