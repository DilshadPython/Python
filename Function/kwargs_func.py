"""
Backwards-compatible wrapper alias for metric_conversion.py (descriptive filename).
"""
from Function.metric_conversion import centimeter

__all__ = ["centimeter"]

if __name__ == '__main__':
    print(centimeter(inches=10, feet=1))
