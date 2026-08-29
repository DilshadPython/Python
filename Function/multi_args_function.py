"""
Demonstrates temperature conversion functions (Fahrenheit <-> Celsius).
"""

def fahrenheit_temp(temp: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (temp - 32.0) * (5.0 / 9.0)

def celsius_temp(temp: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return temp * (9.0 / 5.0) + 32.0

def convert_temp_to(temp: float, to_celsi: str = 'c') -> float:
    """Convert temperature based on target unit ('c' for Celsius, 'f' for Fahrenheit)."""
    if to_celsi.lower() == 'c':
        return fahrenheit_temp(temp)
    else:
        return celsius_temp(temp)

if __name__ == '__main__':
    print("100F to C:", convert_temp_to(100.0, 'c'))
    print("0C to F:", convert_temp_to(0.0, 'f'))
