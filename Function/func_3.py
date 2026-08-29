"""
Backwards-compatible wrapper alias for profile_formatter.py (descriptive filename).
"""
from Function.profile_formatter import profile

__all__ = ["profile"]

if __name__ == '__main__':
    print(profile('Dilshad', 'Abdulla', 'Addr', 'E14', 'London'))
