"""
Manual Next Call Demonstration Script.

This script demonstrates iterating over lists manually using iter() and next().
"""
# "from typing import List, Tuple" imports type hint annotations.
from typing import List, Tuple


def demonstrate_manual_next_calls() -> Tuple[List[int], List[str]]:
    """
    Demonstrate manual next() calls over numbers and car models.

    Returns:
        Tuple[List[int], List[str]]: Extracted elements.
    """
    numbers = [1, 2, 3, 4, 5]
    num_iter = iter(numbers)
    extracted_nums = [next(num_iter), next(num_iter)]

    cars = ["Audi", "Fiat", "Alfa Romeo", "Porsche", "Volvo"]
    car_iter = iter(cars)
    extracted_cars = [next(car_iter), next(car_iter), next(car_iter)]

    return extracted_nums, extracted_cars


if __name__ == "__main__":
    print("=== Manual next() Demonstration ===")
    nums, cars = demonstrate_manual_next_calls()
    print(f"Extracted Numbers : {nums}")
    print(f"Extracted Cars    : {cars}")
