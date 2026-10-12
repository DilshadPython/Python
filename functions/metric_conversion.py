"""
Demonstrates metric conversion functions for length (inches and feet to centimeters).
"""


def centimeter(inches: float = 0.0, feet: float = 0.0) -> float:
    """Convert length given in inches and feet into centimeters."""
    total_inches = inches + (feet * 12.0)
    return total_inches * 2.54


if __name__ == '__main__':
    print("10 in, 1 ft in cm:", centimeter(inches=10, feet=1))
