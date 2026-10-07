"""
Track 09: Modern Backend & API Engineering

Description: Master Senior Python Track 09: Modern Backend & API Engineering. Request lifecycles, CORS, CSRF, Idempotency Keys (SETNX), Jittered Exponential Backoff, and Cursor Pagination.
Level: Senior
URL: http://127.0.0.1:5000/python/senior/modern_backend_api
"""

# --- Code Snippet 1 ---
SameSite=Lax/Strict

# --- Code Snippet 2 ---
# Security Rule: Never allow wildcards when credentials are enabled!
CORS_CONFIG = {
    "allow_origins": ["https://app.teachcloud.dev"],  # Explicit origins ONLY
    "allow_credentials": True,                        # Enables cookies/Auth headers
    "allow_methods": ["GET", "POST", "PUT", "DELETE"],
}

# CSRF Cookie Protection Standard:
COOKIE_OPTIONS = {
    "httponly": True,     # Prevents JavaScript XSS access
    "secure": True,       # Enforces HTTPS transport
    "samesite": "Lax"     # Prevents ambient browser cross-site posting
}

# --- Code Snippet 3 ---
import random

def calculate_jittered_exponential_backoff(attempt: int, base: float = 0.5, max_delay: float = 10.0) -> float:
    """Randomized jitter prevents synchronized client retries from overwhelming recovering services."""
    temp = min(max_delay, base * (2 ** attempt))
    sleep_delay = random.uniform(0, temp)
    return sleep_delay

