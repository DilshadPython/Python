"""
Demonstrates calendar generation using standard library calendar module.
"""
# Import explanation:
# 'import calendar' imports Python standard library calendar module.
import calendar


def get_month_calendar(year: int, month: int) -> str:
    """Return formatted monthly calendar string for specified year and month."""
    return calendar.month(year, month)


if __name__ == "__main__":
    print(get_month_calendar(2026, 8))
