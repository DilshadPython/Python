"""Animal Sounds Demonstration Module.

This module demonstrates class constructors (__init__) and object initialization
using an Animal class hierarchy that produces animal sounds.
"""


class Animal:
    """Class representing an animal with name and sound attributes."""

    def __init__(self, name: str, sound: str) -> None:
        """Initialize Animal with name and sound.

        Args:
            name: Animal species or name.
            sound: Sound produced by the animal.
        """
        self.name: str = name
        self.sound: str = sound

    def make_sound(self) -> str:
        """Return formatted string representing the animal sound.

        Returns:
            Formatted animal sound string.
        """
        return f"The {self.name} makes a '{self.sound}' sound."


if __name__ == "__main__":
    print("=== Animal Sounds Demonstration ===")
    dog = Animal("Dog", "barking")
    cat = Animal("Cat", "meowing")

    print(dog.make_sound())
    print(cat.make_sound())
