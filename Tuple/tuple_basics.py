import collections
import itertools
import operator
import struct
import sys
from typing import Tuple, List, Dict, Any, Union, Optional

Number = Union[int, float]


def starter_tuple_examples() -> Dict[str, Any]:
    """Starter examples demonstrating Python Tuples (tuple) for beginners.
    
    A tuple is an ordered, immutable collection enclosed in parentheses ().
    """
    # 1. Creating tuples
    color_rgb = (255, 128, 0)
    single_element_tuple = ("python",)  # Trailing comma required for 1-element tuple

    # 2. Accessing by index & slicing
    red_val = color_rgb[0]
    green_blue_slice = color_rgb[1:]

    # 3. Tuple packing & unpacking
    lat, lon = 36.1912, 44.0092

    # 4. Immutability verification
    is_immutable = True
    try:
        color_rgb[0] = 200  # type: ignore
        is_immutable = False
    except TypeError:
        is_immutable = True

    return {
        "color_rgb": color_rgb,
        "single_element_tuple": single_element_tuple,
        "extracted_red": red_val,
        "slice_green_blue": green_blue_slice,
        "unpacked_coordinates": (lat, lon),
        "is_immutable_verified": is_immutable
    }


def tuple_packing_and_unpacking(a: Any, b: Any, c: Any) -> Dict[str, Any]:
    """Demonstrates tuple packing, multiple assignment unpacking, extended starred unpacking (*rest), and immutability check."""
    packed_tuple = (a, b, c)
    val1, val2, val3 = packed_tuple
    head, *rest = (a, b, c, "extra1", "extra2")
    
    # Verify immutability by testing TypeError on item assignment
    is_immutable = True
    try:
        packed_tuple[0] = "mutation_attempt"  # type: ignore
        is_immutable = False
    except TypeError:
        is_immutable = True

    return {
        "packed_tuple": packed_tuple,
        "unpacked_values": [val1, val2, val3],
        "extended_head": head,
        "extended_rest": rest,
        "is_immutable": is_immutable
    }


def execute_all_dir_tuple_methods(sample_tuple: Tuple[Any, ...]) -> Dict[str, Any]:
    """Executes all built-in methods from dir(tuple): .count() and .index()."""
    if not isinstance(sample_tuple, tuple):
        raise TypeError("Input must be a tuple")
    
    first_item = sample_tuple[0] if sample_tuple else None
    count_first = sample_tuple.count(first_item) if sample_tuple else 0
    index_first = sample_tuple.index(first_item) if sample_tuple else -1

    return {
        "count_of_first": count_first,
        "index_of_first": index_first,
        "length": len(sample_tuple),
        "tuple_slice": sample_tuple[1:3] if len(sample_tuple) >= 3 else sample_tuple
    }


def tuple_memory_and_namedtuple(data_records: List[Tuple[str, int]]) -> Dict[str, Any]:
    """Demonstrates collections.namedtuple structure and memory efficiency benchmark using sys.getsizeof()."""
    if not isinstance(data_records, list):
        raise TypeError("Input must be a list of tuples")

    Point = collections.namedtuple("Point", ["x", "y"])
    p1 = Point(x=10, y=20)

    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (1, 2, 3, 4, 5)

    return {
        "namedtuple_instance": p1,
        "namedtuple_x": p1.x,
        "namedtuple_y": p1.y,
        "namedtuple_as_dict": p1._asdict(),
        "list_bytes": sys.getsizeof(sample_list),
        "tuple_bytes": sys.getsizeof(sample_tuple),
        "is_tuple_more_lightweight": sys.getsizeof(sample_tuple) < sys.getsizeof(sample_list)
    }


def process_tuple_with_standard_libraries(coords: List[Tuple[int, int]], binary_values: Tuple[int, float]) -> Dict[str, Any]:
    """Demonstrates standard libraries working with tuples: collections.namedtuple, itertools, operator, struct, and sys."""
    if not isinstance(coords, list) or not isinstance(binary_values, tuple):
        raise TypeError("Invalid input types for tuple standard libraries process")

    # 1. collections.namedtuple
    GeoCoord = collections.namedtuple("GeoCoord", ["lat", "lon"])
    location = GeoCoord(lat=36.1912, lon=44.0092)

    # 2. itertools.starmap & itertools.product
    starmap_sums = list(itertools.starmap(lambda x, y: x + y, coords)) if coords else []
    cartesian_prod = list(itertools.product([1, 2], ["a", "b"]))

    # 3. operator.itemgetter sorting
    sorted_tuples = sorted(coords, key=operator.itemgetter(1)) if coords else []

    # 4. struct binary packing/unpacking into tuples
    packed_bytes = struct.pack("if", binary_values[0], binary_values[1])
    unpacked_tuple = struct.unpack("if", packed_bytes)

    return {
        "namedtuple_location": location._asdict(),
        "itertools_starmap_sums": starmap_sums,
        "itertools_cartesian_product": cartesian_prod,
        "operator_sorted_by_second": sorted_tuples,
        "struct_packed_bytes": packed_bytes.hex(),
        "struct_unpacked_tuple": unpacked_tuple
    }
