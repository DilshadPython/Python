"""
Backwards-compatible wrapper alias for email_welcome.py (descriptive filename).
"""
from Function.email_welcome import view_email, welcome

__all__ = ["view_email", "welcome"]

if __name__ == '__main__':
    print(welcome("Tom", "tom@example.com"))
