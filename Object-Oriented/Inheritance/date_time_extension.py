"""Date Time Extension Demonstration Module.

This module demonstrates subclassing Python's standard `datetime.date` class
to add custom domain methods (such as calculating tomorrow's date).
"""

import datetime


class CustomDate(datetime.date):
    """Subclass of datetime.date adding custom date manipulation utility methods."""

    def get_tomorrow(self) -> "CustomDate":
        """Return a new CustomDate object representing tomorrow's date."""
        tomorrow = self + datetime.timedelta(days=1)
        return CustomDate(tomorrow.year, tomorrow.month, tomorrow.day)


if __name__ == "__main__":
    print("=== Custom Date Extension Demonstration ===")
    today = CustomDate(2026, 8, 30)
    print("Today:", today)
    print("Tomorrow:", today.get_tomorrow())
