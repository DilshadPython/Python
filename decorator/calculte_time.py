"""Legacy module alias forwarding to calculate_time.py."""

from decorator.calculate_time import (
    time_you_need,
    walking_to_work,
    walking_to_works,
    walking_to_university,
    walking_home,
)

if __name__ == "__main__":
    walking_to_work("work")
    walking_to_university("University")
    walking_home("home")
