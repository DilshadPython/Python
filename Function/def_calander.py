"""
Backwards-compatible wrapper alias for def_calendar.py (corrected spelling).
"""
from Function.def_calendar import get_month_calendar

__all__ = ["get_month_calendar"]

if __name__ == "__main__":
    print(get_month_calendar(2026, 8))
