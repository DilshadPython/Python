"""
Section 2: Pythonic Programming & Clean Code Architecture

Description: Master Pythonic programming principles: PEP 8, Zen of Python (PEP 20), DRY, KISS, Separation of Concerns, Dependency Injection, Composition vs Inheritance, and Django design philosophy.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/pythonic_programming
"""

# --- Code Snippet 1 ---
# Imperative loop accumulator
users = []

for user in all_users:
    if user.is_active:
        users.append(user)

# --- Code Snippet 2 ---
# Single-line list comprehension
users = [user for user in all_users if user.is_active]

# --- Code Snippet 3 ---
# Pythonic does NOT mean cramming logic into one line.
# Clean, readable multi-line formatting with explicit type annotations:
def get_active_users(users: list[User]) -> list[User]:
    """Filter and return active users from the provided user collection."""
    return [
        user
        for user in users
        if user.is_active
    ]

