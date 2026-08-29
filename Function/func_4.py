"""
Backwards-compatible wrapper alias for user_greeting.py (descriptive filename).
"""
from Function.user_greeting import greet_user

__all__ = ["greet_user"]

if __name__ == '__main__':
    print(greet_user("Dilshad"))
