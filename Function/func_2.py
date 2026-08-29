"""
Backwards-compatible wrapper alias for gender_mapping.py (descriptive filename).
"""
from Function.gender_mapping import get_gender

__all__ = ["get_gender"]

if __name__ == '__main__':
    print("Input 'm':", get_gender('m'))
