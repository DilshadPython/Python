"""
Pandas pd.date_range() vs Python range() Comparison Module.

This module demonstrates:
- Built-in Python range(start, stop, step) sequence generation.
- Pandas pd.date_range(start, end, periods, freq) date sequence generation.
- Handling temporal frequencies ('D' Daily, 'B' Business Days, 'ME' Month End, 'h' Hourly).
- Pandas pd.RangeIndex structure for memory-efficient integer indexing.
"""

# Import pandas for date range sequence and Index structures
import pandas as pd


def generate_python_range(start: int, stop: int, step: int = 1) -> range:
    """Generate a standard Python built-in range sequence.

    Args:
        start (int): Start boundary integer.
        stop (int): Exclusive stop boundary integer.
        step (int, optional): Step delta integer. Defaults to 1.

    Returns:
        range: Built-in Python range object.
    """
    return range(start, stop, step)


def generate_pandas_date_range(
    start: str, periods: int | None = None, end: str | None = None, freq: str = "D"
) -> pd.DatetimeIndex:
    """Generate a Pandas DatetimeIndex sequence using pd.date_range().

    Args:
        start (str): Start date string (ISO format).
        periods (int | None, optional): Total number of timestamps to generate. Defaults to None.
        end (str | None, optional): End date string. Defaults to None.
        freq (str, optional): Frequency string ('D', 'B', 'ME', 'h'). Defaults to "D".

    Returns:
        pd.DatetimeIndex: DatetimeIndex object.
    """
    return pd.date_range(start=start, end=end, periods=periods, freq=freq)


def generate_pandas_range_index(start: int, stop: int, step: int = 1) -> pd.RangeIndex:
    """Create an optimized Pandas RangeIndex structure.

    Args:
        start (int): Start integer boundary.
        stop (int): Stop integer boundary.
        step (int, optional): Step increment. Defaults to 1.

    Returns:
        pd.RangeIndex: Memory-optimized range index.
    """
    return pd.RangeIndex(start=start, stop=stop, step=step)


if __name__ == "__main__":
    py_rng = generate_python_range(1, 10, 2)
    print("--- Built-in Python range(1, 10, 2) ---")
    print(py_rng, "List:", list(py_rng))

    daily_dates = generate_pandas_date_range(start="2026-01-01", periods=5, freq="D")
    print("\n--- Pandas pd.date_range (Daily 'D') ---")
    print(daily_dates)

    business_dates = generate_pandas_date_range(start="2026-01-01", periods=5, freq="B")
    print("\n--- Pandas pd.date_range (Business Days 'B') ---")
    print(business_dates)

    pd_rng_idx = generate_pandas_range_index(0, 1000, 5)
    print("\n--- Pandas RangeIndex ---")
    print(pd_rng_idx)
