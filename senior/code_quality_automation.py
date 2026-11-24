"""
Track 13: Industrial Code Quality & Automation

Description: Master Senior Python Track 13: Industrial Code Quality & Automation. Ruff unified linting/formatting, pyproject.toml rules, and multi-tiered CI safety nets.
Level: Senior
URL: http://127.0.0.1:5000/python/senior/code_quality_automation
"""

# --- Code Snippet 1 ---
# pyproject.toml configuration for Ruff
[tool.ruff]
target-version = "py312"
line-length = 88

[tool.ruff.lint]
select = [
    "E", "W",  # pycodestyle errors & warnings
    "F",       # Pyflakes
    "I",       # isort import ordering
    "B",       # flake8-bugbear (mutable defaults, traps)
    "UP",      # pyupgrade syntax modernization
    "S",       # flake8-bandit security auditing
    "C4",      # flake8-comprehensions efficiency
    "ASYNC",   # flake8-async event loop traps
]

