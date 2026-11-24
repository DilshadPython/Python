"""
Built-In Container Iterators Module.

This module demonstrates iteration mechanics across Python's built-in container types:
- Sequence iterators: list_iterator, tuple_iterator, str_iterator
- Mapping iterators: dict_keyiterator, dict_valueiterator, dict_itemiterator
- File handle iterators: Memory-efficient line-by-line file streaming
"""
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path
# "from typing import Dict, List, Tuple, Any" imports typing annotations.
from typing import Dict, List, Tuple, Any


def iterate_dictionary_views(data_dict: Dict[str, Any]) -> Dict[str, List[Any]]:
    """
    Demonstrate iterating over dictionary keys, values, and key-value items.

    Args:
        data_dict (Dict[str, Any]): Sample dictionary.

    Returns:
        Dict[str, List[Any]]: Lists of keys, values, and items extracted via iterators.
    """
    key_iter = iter(data_dict.keys())
    val_iter = iter(data_dict.values())
    item_iter = iter(data_dict.items())

    keys = [next(key_iter) for _ in range(len(data_dict))]
    values = [next(val_iter) for _ in range(len(data_dict))]
    items = [next(item_iter) for _ in range(len(data_dict))]

    return {
        "keys": keys,
        "values": values,
        "items": items,
    }


def iterate_file_lines(file_path: Path) -> List[str]:
    """
    Demonstrate memory-friendly file line iteration using built-in file object iterator.

    File objects implement the iterator protocol directly, yielding lines lazily one by one
    without loading the entire file into RAM.

    Args:
        file_path (Path): Path to text file.

    Returns:
        List[str]: List of stripped lines read from file.
    """
    lines: List[str] = []
    if not file_path.exists():
        return lines

    with open(file_path, "r", encoding="utf-8") as f:
        # File object 'f' is its own iterator
        for line in f:
            lines.append(line.strip())
    return lines


def iterate_tuples_and_strings(text: str, tpl: Tuple[Any, ...]) -> Dict[str, List[Any]]:
    """
    Demonstrate str_iterator and tuple_iterator.

    Args:
        text (str): Sample text string.
        tpl (Tuple[Any, ...]): Sample tuple sequence.

    Returns:
        Dict[str, List[Any]]: Extracted character and tuple element lists.
    """
    char_iter = iter(text)
    tuple_iter = iter(tpl)

    return {
        "chars": [next(char_iter) for _ in range(len(text))],
        "tuple_elements": [next(tuple_iter) for _ in range(len(tpl))],
    }


if __name__ == "__main__":
    print("=== Step 1: Built-In Container Iterators ===")
    sample_dict = {"Alan": 23, "Sara": 30, "Tom": 28}

    dict_res = iterate_dictionary_views(sample_dict)
    print(f"Dictionary view iterators : {dict_res}")

    seq_res = iterate_tuples_and_strings("Python", (10, 20, 30))
    print(f"String & Tuple iterators   : {seq_res}")

    sample_file = Path(__file__).parent.parent / "grade.txt"
    if sample_file.exists():
        file_lines = iterate_file_lines(sample_file)
        print(f"File line iterator ({sample_file.name}): {file_lines}")
