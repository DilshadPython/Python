# from typing import List, Dict, Tuple, Union, Optional, Any: Built-in typing module.
import itertools
import sys
from typing import List, Dict, Tuple, Union, Optional, Any

# Type Alias for numeric types in comprehension processing
Number = Union[int, float]


def starter_list_comprehension_examples() -> Dict[str, Any]:
    """Starter examples demonstrating List Comprehensions for beginners.
    
    Syntax: [expression for item in iterable if condition]
    """
    # 1. Basic transformation: Square numbers from 1 to 5
    squares = [x ** 2 for x in range(1, 6)]

    # 2. Conditional filtering: Extract even numbers from 1 to 10
    evens = [x for x in range(1, 11) if x % 2 == 0]

    # 3. String manipulation: Convert words to uppercase
    words = ["hello", "cloud", "flask", "python"]
    uppercase_words = [word.upper() for word in words]

    # 4. Ternary mapping: Label numbers as 'Even' or 'Odd'
    number_labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]

    return {
        "squares": squares,
        "evens": evens,
        "uppercase_words": uppercase_words,
        "number_labels": number_labels
    }


def basic_and_conditional_comprehensions(
    numbers: List[Number],
    threshold: Number = 0
) -> Dict[str, List[Any]]:
    """Demonstrates basic list comprehensions, filtering with 'if', and ternary 'if-else' mapping."""
    # Example Call: basic_and_conditional_comprehensions([1, -2, 3, -4, 5], threshold=0)
    # Explanation: Transforms numbers with squares, filters positive numbers, and maps negative numbers to 0.
    if not isinstance(numbers, list):
        raise TypeError("Input 'numbers' must be a valid Python list")

    for val in numbers:
        if not isinstance(val, (int, float)):
            raise TypeError("All items in 'numbers' list must be integer or float")

    # 1. Basic Transformation: [expression for item in iterable]
    squared = [x ** 2 for x in numbers]

    # 2. Conditional Filtering: [expression for item in iterable if condition]
    filtered_positive = [x for x in numbers if x > threshold]

    # 3. Conditional Expression (Ternary Mapping): [x if condition else default for x in iterable]
    clamped_zeros = [x if x >= 0 else 0 for x in numbers]

    # 4. String Formatting in Comprehension: [f-string for item in iterable]
    formatted_labels = [f"Val:{x}" for x in numbers]

    return {
        "squared": squared,
        "filtered_positive": filtered_positive,
        "clamped_zeros": clamped_zeros,
        "formatted_labels": formatted_labels
    }


def nested_and_matrix_comprehensions(
    matrix: List[List[Any]]
) -> Dict[str, Any]:
    """Demonstrates 2D matrix flattening, transposing, and nested conditional filtering in comprehensions."""
    # Example Call: nested_and_matrix_comprehensions([[1, 2], [3, 4]])
    # Explanation: Flattens 2D grid to 1D list and transposes rows into columns.
    if not isinstance(matrix, list):
        raise TypeError("Input 'matrix' must be a list of lists")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("All items in 'matrix' must be sub-lists")

    # 1. Matrix Flattening: [element for row in matrix for element in row]
    flattened = [element for row in matrix for element in row]

    # 2. Matrix Transpose: [[row[i] for row in matrix] for i in range(cols)]
    if matrix and all(len(row) == len(matrix[0]) for row in matrix):
        cols = len(matrix[0])
        transposed = [[row[i] for row in matrix] for i in range(cols)]
    else:
        transposed = []

    # 3. Nested Conditional Filter: [x for row in matrix for x in row if isinstance(x, (int, float)) and x > 0]
    positive_numeric = [
        val for row in matrix for val in row
        if isinstance(val, (int, float)) and val > 0
    ]

    return {
        "flattened": flattened,
        "transposed": transposed,
        "positive_numeric": positive_numeric
    }


def dict_set_and_generator_comprehensions(
    items: List[Any]
) -> Dict[str, Any]:
    """Demonstrates dictionary comprehensions, set comprehensions, and generator expressions memory metrics."""
    # Example Call: dict_set_and_generator_comprehensions(["apple", "banana", "apple", "cherry"])
    # Explanation: Builds frequency maps, unique set collections, and compares memory sizes via sys.getsizeof().
    if not isinstance(items, list):
        raise TypeError("Input 'items' must be a valid Python list")

    # 1. Dictionary Comprehension: {key_expr: value_expr for item in iterable}
    length_dict = {str(item): len(str(item)) for item in items}

    # 2. Set Comprehension: {expression for item in iterable} (removes duplicates automatically)
    unique_upper_set = {str(item).upper() for item in items}

    # 3. Generator Expression vs List Comprehension Memory Benchmark
    large_range = range(10000)
    list_comp = [x ** 2 for x in large_range]
    gen_expr = (x ** 2 for x in large_range)

    list_memory_bytes = sys.getsizeof(list_comp)
    gen_memory_bytes = sys.getsizeof(gen_expr)

    return {
        "length_dict": length_dict,
        "unique_upper_set": sorted(list(unique_upper_set)),
        "list_memory_bytes": list_memory_bytes,
        "gen_memory_bytes": gen_memory_bytes,
        "is_generator_lazy": gen_memory_bytes < list_memory_bytes
    }


def comprehension_vs_standard_libraries(
    numbers: List[int]
) -> Dict[str, Any]:
    """Compares list comprehensions against functional built-ins (map, filter, any, all) and itertools (starmap, compress)."""
    # Example Call: comprehension_vs_standard_libraries([1, 2, 3, 4, 5])
    if not isinstance(numbers, list):
        raise TypeError("Input 'numbers' must be a valid Python list")

    # 1. Map vs List Comprehension
    map_result = list(map(lambda x: x * 2, numbers))
    comp_map_result = [x * 2 for x in numbers]

    # 2. Filter vs List Comprehension
    filter_result = list(filter(lambda x: x % 2 == 0, numbers))
    comp_filter_result = [x for x in numbers if x % 2 == 0]

    # 3. itertools.starmap vs Multi-variable Comprehension
    tuple_pairs = [(a, a + 1) for a in numbers[:3]]
    starmap_result = list(itertools.starmap(lambda a, b: a * b, tuple_pairs))
    comp_starmap_result = [a * b for a, b in tuple_pairs]

    # 4. itertools.compress vs Zip Comprehension
    selectors = [True, False, True, True, False]
    compress_result = list(itertools.compress(numbers, selectors))
    comp_compress_result = [num for num, sel in zip(numbers, selectors) if sel]

    # 5. any() and all() evaluation with generator expressions
    has_even = any(x % 2 == 0 for x in numbers)
    all_positive = all(x > 0 for x in numbers)

    return {
        "map_equals_comprehension": map_result == comp_map_result,
        "filter_equals_comprehension": filter_result == comp_filter_result,
        "starmap_equals_comprehension": starmap_result == comp_starmap_result,
        "compress_equals_comprehension": compress_result == comp_compress_result,
        "has_even": has_even,
        "all_positive": all_positive
    }
