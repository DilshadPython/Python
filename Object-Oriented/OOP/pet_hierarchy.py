"""Pet Hierarchy Demonstration Module.

This module demonstrates class instantiation and inheritance with `Dog` and `Cat` classes.
"""


class Dog:
    """Base Dog class with attributes for name, age, color, and gender."""

    def __init__(self, name: str, age: int, color: str, gender: str) -> None:
        """Initialize Dog instance."""
        self.name: str = name
        self.age: int = age
        self.color: str = color
        self.gender: str = gender
        self.weight: float = 0.0

    def description(self) -> str:
        """Return formatted description string."""
        return f"Dog '{self.name}', Age: {self.age}, Color: {self.color}, Gender: {self.gender}."

    def speak(self) -> str:
        """Return dog bark sound."""
        return "Bark!"

    def set_weight(self, weight: float) -> None:
        """Set dog weight."""
        self.weight = float(weight)


class Cat(Dog):
    """Cat subclass inheriting from Dog base pet class."""

    def __init__(self, name: str, age: int, color: str, gender: str) -> None:
        """Initialize Cat instance using super().__init__()."""
        super().__init__(name, age, color, gender)

    def speak(self) -> str:
        """Override speak() to return cat meow sound."""
        return "Meow!"


if __name__ == "__main__":
    print("=== Pet Hierarchy Demonstration ===")
    dog = Dog("Raffi", 8, "white", "male")
    cat = Cat("Mimi", 2, "black", "female")

    print(dog.description(), "| Sound:", dog.speak())
    print(cat.description(), "| Sound:", cat.speak())
