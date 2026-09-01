# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import sys: Standard library module for CPython memory inspection (sys.getsizeof).
# - import datetime: Standard library module for datetime formatting specifiers (%B, %d, %j, %A).
# - from typing import Dict, List, Any, Tuple, Union, Optional: PEP 484 type annotations.
# =========================================================================
import datetime
import sys
from typing import Any, Dict, List, Optional, Tuple, Union

Number = Union[int, float]


def starter_range_examples() -> Dict[str, Any]:
    """
    Starter examples demonstrating Python range sequence generation,
    positional parameters (start, stop, step), negative countdowns, and grid loops.
    """
    # 1. Single parameter: range(stop) -> 0 to stop-1
    stop_seq = list(range(5))

    # 2. Two parameters: range(start, stop) -> start to stop-1
    start_stop_seq = list(range(2, 8))

    # 3. Three parameters: range(start, stop, step)
    step_seq = list(range(1, 10, 2))

    # 4. Negative step countdown
    countdown_seq = list(range(10, 0, -2))

    # 5. Grid sequence generation (nested range loops)
    grid_matrix: List[List[int]] = []
    for r in range(3):
        row: List[int] = []
        for c in range(4):
            row.append(r * 4 + c)
        grid_matrix.append(row)

    # 6. Horizontal string representation
    horizontal_str = " -> ".join(str(x) for x in range(1, 6))

    return {
        "stop_sequence": stop_seq,
        "start_stop_sequence": start_stop_seq,
        "step_sequence": step_seq,
        "countdown_sequence": countdown_seq,
        "grid_matrix": grid_matrix,
        "horizontal_sequence": horizontal_str,
    }


def range_and_number_formatting(
    limit: int = 5,
    large_number: int = 1000000,
    float_val: float = 123.45678,
) -> Dict[str, Any]:
    """
    Demonstrates range-driven zero-padded string iteration (01, 02...),
    float precision formatting, and thousand separators for large integers.
    """
    if not isinstance(limit, int) or limit < 0:
        raise TypeError("Input 'limit' must be a non-negative integer")
    if not isinstance(large_number, int):
        raise TypeError("Input 'large_number' must be an integer")
    if not isinstance(float_val, (int, float)):
        raise TypeError("Input 'float_val' must be a numeric value")

    # 1. Zero-padded string iteration with range()
    zero_padded_list = [f"{i:02d}" for i in range(1, limit + 1)]
    custom_padded_list = [f"ITEM_{i:04d}" for i in range(1, limit + 1)]

    # 2. Precision float formatting
    formatted_float_2dp = f"{float_val:.2f}"
    formatted_float_4dp = f"{float_val:.4f}"

    # 3. Large integer thousand separators
    formatted_large_comma = f"{large_number:,}"
    formatted_large_underscore = f"{large_number:_}"

    return {
        "zero_padded_items": zero_padded_list,
        "custom_padded_items": custom_padded_list,
        "formatted_float_2dp": formatted_float_2dp,
        "formatted_float_4dp": formatted_float_4dp,
        "formatted_large_comma": formatted_large_comma,
        "formatted_large_underscore": formatted_large_underscore,
    }


def datetime_and_graphics_formatting(
    days_count: int = 5,
    pyramid_height: int = 4,
) -> Dict[str, Any]:
    """
    Demonstrates datetime formatting (%B, %d, %j, %A) over range intervals
    and 3D ASCII graphic pattern generation (pyramids, single-sided, decreasing spaces).
    """
    if not isinstance(days_count, int) or days_count <= 0:
        raise TypeError("Input 'days_count' must be a positive integer")
    if not isinstance(pyramid_height, int) or pyramid_height <= 0:
        raise TypeError("Input 'pyramid_height' must be a positive integer")

    # 1. Datetime formatting over range() days
    base_date = datetime.datetime(2026, 1, 1)
    formatted_dates: List[Dict[str, str]] = []

    for day_offset in range(days_count):
        current_date = base_date + datetime.timedelta(days=day_offset)
        formatted_dates.append({
            "iso": current_date.strftime("%Y-%m-%d"),
            "full_date": current_date.strftime("%A, %B %d, %Y"),
            "day_of_year": current_date.strftime("Day %j"),
        })

    # 2. ASCII Standard Centered Pyramid
    pyramid_lines: List[str] = []
    for i in range(1, pyramid_height + 1):
        spaces = " " * (pyramid_height - i)
        stars = "*" * (2 * i - 1)
        pyramid_lines.append(f"{spaces}{stars}")

    # 3. ASCII Single-Sided Left-Aligned Pyramid
    single_sided_lines: List[str] = []
    for i in range(1, pyramid_height + 1):
        single_sided_lines.append("*" * i)

    # 4. ASCII Decreasing Space Inverted Pattern
    decreasing_space_lines: List[str] = []
    for i in range(pyramid_height, 0, -1):
        spaces = " " * (pyramid_height - i)
        hashes = "#" * i
        decreasing_space_lines.append(f"{spaces}{hashes}")

    return {
        "formatted_dates": formatted_dates,
        "ascii_pyramid": pyramid_lines,
        "ascii_single_sided": single_sided_lines,
        "ascii_decreasing_space": decreasing_space_lines,
    }


def range_vs_xrange_mechanics(
    sample_val: int = 5,
) -> Dict[str, Any]:
    """
    Demonstrates dir(range) methods & attributes (.start, .stop, .step, .index(), .count()),
    O(1) constant memory overhead benchmarks (sys.getsizeof),
    O(1) containment arithmetic evaluation, and Python 2 xrange vs Python 3 range comparison.
    """
    # Create sample range object
    r = range(2, 20, 3)  # [2, 5, 8, 11, 14, 17]

    # 1. Access range sequence attributes
    range_start = r.start
    range_stop = r.stop
    range_step = r.step
    range_length = len(r)

    # 2. Sequence methods: .index() and .count()
    index_of_8 = r.index(8) if 8 in r else -1
    count_of_8 = r.count(8)
    count_of_99 = r.count(99)

    # 3. O(1) Containment testing vs List O(N)
    in_range = 14 in r
    not_in_range = 7 in r

    # 4. O(1) Memory overhead comparison
    range_1k = range(1000)
    range_1m = range(1000000)
    list_1k = list(range(1000))

    range_1k_size = sys.getsizeof(range_1k)
    range_1m_size = sys.getsizeof(range_1m)
    list_1k_size = sys.getsizeof(list_1k)

    # Memory allocation is constant O(1) regardless of scale
    is_constant_memory = range_1k_size == range_1m_size

    # 5. Range Equality comparison (Python 3.3+)
    # Empty ranges with different bounds are equal
    eq_empty = range(0) == range(2, 1, 3)
    # Range sequence equality
    eq_seq = range(0, 10, 2) == range(0, 9, 2)

    # 6. Introspection: Extract public methods from dir(range)
    dir_range_public = [m for m in dir(range) if not m.startswith("_")]

    return {
        "range_attributes": {
            "start": range_start,
            "stop": range_stop,
            "step": range_step,
            "length": range_length,
        },
        "sequence_methods": {
            "index_of_8": index_of_8,
            "count_of_8": count_of_8,
            "count_of_99": count_of_99,
        },
        "containment_test": {
            "in_range": in_range,
            "not_in_range": not_in_range,
        },
        "memory_benchmark": {
            "range_1k_bytes": range_1k_size,
            "range_1m_bytes": range_1m_size,
            "list_1k_bytes": list_1k_size,
            "is_constant_memory": is_constant_memory,
        },
        "range_equality": {
            "empty_ranges_equal": eq_empty,
            "equivalent_ranges_equal": eq_seq,
        },
        "dir_range_public_methods": sorted(dir_range_public),
        "python2_vs_3_notes": (
            "In Python 2.7, range() generated an eager list (O(N) memory), "
            "whereas xrange() was a special sequence generator object (O(1) memory). "
            "In Python 3.0+, xrange() was removed and range() became an immutable, "
            "lazy sequence object operating with fixed O(1) memory."
        ),
    }
