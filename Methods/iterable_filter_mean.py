"""
Demonstrates filtering numeric sequences relative to statistical mean using built-in filter().
"""
# "from module import name" imports specific type hint symbols directly into local scope.
import statistics
from typing import List, Tuple


def filter_numbers_by_mean(data: List[float]) -> Tuple[float, List[float], List[float]]:
    """
    Calculate statistical mean of numbers and filter values above and below the average.
    
    Args:
        data (List[float]): List of floating point values.
        
    Returns:
        Tuple[float, List[float], List[float]]: Tuple containing (mean, above_mean, below_mean).
    """
    if not data:
        return 0.0, [], []
    avg: float = statistics.mean(data)
    above_mean: List[float] = list(filter(lambda x: x > avg, data))
    below_mean: List[float] = list(filter(lambda x: x < avg, data))
    return avg, above_mean, below_mean


if __name__ == '__main__':
    sample_data: List[float] = [2.3, 12.0, -0.7, 6.7, 3.13, 22.03, 9.11]
    mean_val, above, below = filter_numbers_by_mean(sample_data)
    print(f"Mean Average: {mean_val:.2f}")
    print("Above Mean:", above)
    print("Below Mean:", below)
