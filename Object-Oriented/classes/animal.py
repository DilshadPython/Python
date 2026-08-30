"""Legacy Animal Script (Refactored).

This module updates the original `animal.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
"""


class Animal:
    """Animal class with name and sound attributes."""

    def __init__(self, name: str, sound: str) -> None:
        """Initialize Animal."""
        self.name: str = name
        self.sound: str = sound

    def sound_say(self) -> str:
        """Return formatted sound string."""
        return f"The {self.name} sound is {self.sound}."


if __name__ == "__main__":
    dogy = Animal("Dog", "barking")
    caty = Animal("Cat", "meowing")
    print(dogy.sound_say())
    print(caty.sound_say())
