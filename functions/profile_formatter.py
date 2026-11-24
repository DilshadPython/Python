"""
Demonstrates formatting user profile details using string formatting methods.
"""


def profile(fname: str, lname: str, address: str, postcode: str, city: str) -> str:
    """Format and return profile summary string."""
    return f"First name: {fname}\nLast name: {lname}\nAddress: {address}\nPostcode: {postcode}\nCity: {city}"


if __name__ == '__main__':
    user_prof = profile('John', 'Smith', '6 Ursula Gould Way', 'E14 7FX', 'London')
    print(user_prof)
