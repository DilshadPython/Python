"""
Advanced Object-Oriented Programming: Static Utility Methods.

This module demonstrates using `@staticmethod` decorators to define pure utility functions
logically grouped inside a class namespace without accessing instance (`self`) or class (`cls`) state.
"""
# "import module" loads datetime module from standard library into namespace.
import datetime


class WorkCalendar:
    """Class namespace housing static date calculation utilities."""

    @staticmethod
    def is_workday(day: datetime.date) -> bool:
        """
        Check if a given date falls on a weekday (Monday-Friday).

        Args:
            day (datetime.date): Date object to evaluate.

        Returns:
            bool: True if Monday through Friday, False if Saturday or Sunday.
        """
        # weekday(): Monday is 0, Sunday is 6
        return day.weekday() < 5

    @staticmethod
    def calculate_workdays_between(start_date: datetime.date, end_date: datetime.date) -> int:
        """
        Calculate total workdays between start_date and end_date (inclusive).

        Args:
            start_date (datetime.date): Beginning date.
            end_date (datetime.date): Ending date.

        Returns:
            int: Number of business workdays.
        """
        if start_date > end_date:
            raise ValueError("Start date cannot be after end date.")

        current = start_date
        workdays = 0
        while current <= end_date:
            if current.weekday() < 5:
                workdays += 1
            current += datetime.timedelta(days=1)
        return workdays
