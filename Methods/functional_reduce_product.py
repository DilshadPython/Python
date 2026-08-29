"""
Demonstrates sequence reduction and cumulative product using functools.reduce().
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from functools import reduce
from typing import List, Union

Numeric = Union[int, float]


def calculate_cumulative_product(numbers: List[Numeric]) -> Numeric:
    """
    Compute cumulative product of all elements in a numeric list using reduce().
    
    Args:
        numbers (List[Numeric]): List of numeric elements.
        
    Returns:
        Numeric: Cumulative product.
    """
    if not numbers:
        return 0
    return reduce(lambda x, y: x * y, numbers)


if __name__ == '__main__':
    sample_numbers: List[Numeric] = [2.3, 12.0, -0.7, 6.7, 3.13]
    prod = calculate_cumulative_product(sample_numbers)
    print("Cumulative Product via reduce():", prod)
