"""
Demonstrates skipping zero denominators using continue and terminating on sentinel (-1).
"""
from typing import List, Optional, Tuple


def process_division_pairs(pairs: List[Tuple[float, float]]) -> List[Optional[float]]:
    """Compute division for pairs, skipping zero denominator with continue logic and breaking on -1."""
    results: List[Optional[float]] = []

    for num, den in pairs:
        if den == -1:
            break
        if den == 0:
            continue
        results.append(num / den)

    return results


if __name__ == '__main__':
    test_pairs = [(10.0, 2.0), (5.0, 0.0), (20.0, 4.0), (8.0, -1.0)]
    out = process_division_pairs(test_pairs)
    print("Division results (skipping divide-by-zero):", out)
