"""
Backwards-compatible wrapper alias for gender_translator.py (descriptive filename).
"""
from Function.gender_translator import get_gender

__all__ = ["get_gender"]

if __name__ == '__main__':
    print("Gender 'm':", get_gender('m'))
