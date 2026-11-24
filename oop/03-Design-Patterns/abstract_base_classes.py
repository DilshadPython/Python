"""
Advanced Object-Oriented Programming: Abstract Base Classes (ABCs).

This module demonstrates enforcing interface contracts on derived subclasses using `abc.ABC`
and `@abstractmethod` decorators for polymorphic geometric calculations.
"""
# "import module" loads math module into namespace.
import math
# "from module import name" imports ABC and abstractmethod from standard library.
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract Base Class defining interface contract for geometric shapes."""

    @abstractmethod
    def area(self) -> float:
        """Abstract method calculating shape area (must be implemented by subclasses)."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Abstract method calculating shape perimeter (must be implemented by subclasses)."""
        pass


class Circle(Shape):
    """Circle implementation satisfying Shape interface contract."""

    def __init__(self, radius: float) -> None:
        """Initialize Circle with radius."""
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius: float = float(radius)

    def area(self) -> float:
        """Calculate circle area (pi * r^2)."""
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        """Calculate circle perimeter / circumference (2 * pi * r)."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle implementation satisfying Shape interface contract."""

    def __init__(self, width: float, height: float) -> None:
        """Initialize Rectangle with width and height."""
        if width < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative.")
        self.width: float = float(width)
        self.height: float = float(height)

    def area(self) -> float:
        """Calculate rectangle area (width * height)."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate rectangle perimeter (2 * (width + height))."""
        return 2 * (self.width + self.height)
