"""
Python Easter Egg: `import antigravity` (XKCD Comic #353 & Geohashing)

Importing `antigravity` triggers a side effect: opening the famous XKCD comic #353
("Python") in the system default web browser.

Module Attributes & Functions:
- `antigravity.geohash`: Calculates a geohash location based on latitude, longitude,
  and the Dow Jones Industrial Average opening price (XKCD comic #426).

Example:
    >>> import antigravity
    >>> antigravity.geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
    37.857713 -122.544543
"""
import antigravity


def calculate_geohash(lat: float, lon: float, datedow: bytes) -> None:
    """
    Computes and prints an XKCD #426 geohash coordinate using `antigravity.geohash`.

    Args:
        lat (float): Latitude coordinate (e.g. 37.421542).
        lon (float): Longitude coordinate (e.g. -122.085589).
        datedow (bytes): Date string concatenated with opening Dow Jones price as bytes
                         (e.g. b'2005-05-26-10458.68').
    """
    print(f"Calculating geohash for Lat: {lat}, Lon: {lon}, Date-Dow: {datedow.decode('utf-8')}:")
    antigravity.geohash(lat, lon, datedow)


def main() -> None:
    """Executes the antigravity Easter egg demonstration."""
    print("=" * 60)
    print("🚀 Python Easter Egg: Flying with Python (`import antigravity`)")
    print("=" * 60)
    print("\n1. Web Browser Side-Effect:")
    print("   Importing 'antigravity' opens: https://xkcd.com/353/")

    print("\n2. XKCD #426 Geohashing Function Demonstration:")
    # Sample coordinates: Googleplex (37.422, -122.084) with benchmark datedow
    calculate_geohash(37.421542, -122.085589, b"2005-05-26-10458.68")


if __name__ == "__main__":
    main()
