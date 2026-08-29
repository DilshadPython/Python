"""
Demonstrates map() transformation of temperature tuples from Celsius to Fahrenheit.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import List, Tuple

# Type alias for (City, Celsius) tuple
CityTemperature = Tuple[str, float]


def convert_celsius_to_fahrenheit(cities_celsius: List[CityTemperature]) -> List[CityTemperature]:
    """
    Convert a list of (city_name, celsius_temp) tuples into (city_name, fahrenheit_temp).
    
    Formula: F = (9/5) * C + 32
    
    Args:
        cities_celsius (List[CityTemperature]): Input tuple list.
        
    Returns:
        List[CityTemperature]: Transformed tuple list in Fahrenheit.
    """
    fahrenheit_map = map(lambda data: (data[0], round((9 / 5) * data[1] + 32, 2)), cities_celsius)
    return list(fahrenheit_map)


if __name__ == '__main__':
    temperatures_c: List[CityTemperature] = [
        ('Moscow', -16),
        ('Warsaw', -9),
        ('New York', 13),
        ('Cairo', 22),
        ('Dubai', 25),
        ('Erbil', 18),
        ('London', 12),
        ('Rome', 15),
        ('Paris', 14),
    ]
    print("Fahrenheit Temperatures:", convert_celsius_to_fahrenheit(temperatures_c))
