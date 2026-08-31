"""
Local vs Global Scope and Shadowing (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: Local variable assignments inside functions shadow global variables
  unless explicitly overridden with `global`.
"""

from __future__ import print_function

name = 'Dilshad'
first_name = 'Tomas'
year = 1978
language = 'Python'


def get_global_name():
    """Reads global variable 'name'."""
    return "My name is " + name


def test_local_shadowing_first_name():
    """Demonstrates that assigning first_name locally does not mutate global first_name."""
    local_first_name = 'Julia'
    return {
        "local": local_first_name,
        "global": first_name
    }


def get_age_comparison():
    """Calculates age strings with local shadowing vs global value."""
    local_year = 1975
    return {
        "local_year_str": "My age is " + str(local_year),
        "global_year_str": "But my age here is " + str(year)
    }


def run_demo():
    """Runs scope shadowing demonstration."""
    print(get_global_name())

    shadow = test_local_shadowing_first_name()
    print("Local shadowed first name:", shadow["local"])
    print("Global first name unchanged:", shadow["global"])

    ages = get_age_comparison()
    print(ages["local_year_str"])
    print(ages["global_year_str"])

    return shadow


if __name__ == '__main__':
    run_demo()