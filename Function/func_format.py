"""
Backwards-compatible wrapper alias for formatted_greeting.py (descriptive filename).
"""
from Function.formatted_greeting import welcome_msg, user_details

__all__ = ["welcome_msg", "user_details"]

if __name__ == '__main__':
    print(welcome_msg('Hello, '))
