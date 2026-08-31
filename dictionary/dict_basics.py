import collections
import json
import operator
import sys
import types
from typing import Dict, List, Any, Union, Optional, Tuple

Number = Union[int, float]


def starter_dict_examples() -> Dict[str, Any]:
    """Starter examples demonstrating Python Dictionaries (dict) for beginners.
    
    A dictionary is a mutable collection of key-value pairs where keys are unique and hashable.
    """
    # 1. Creating dictionaries
    user_profile = {"username": "coder_starter", "level": "Beginner", "score": 100}
    empty_dict: Dict[str, Any] = {}

    # 2. Accessing values safely
    user_name = user_profile["username"]
    user_role = user_profile.get("role", "Guest")  # Safe fallback if key missing

    # 3. Adding and modifying key-value pairs
    user_profile["score"] = 150  # Update existing value
    user_profile["language"] = "Python"  # Add new key-value pair

    # 4. Dictionary key membership check & key/value lists
    has_score = "score" in user_profile
    all_keys = list(user_profile.keys())
    all_values = [str(v) for v in user_profile.values()]

    return {
        "user_profile": user_profile,
        "empty_dict": empty_dict,
        "accessed_username": user_name,
        "safe_get_role": user_role,
        "has_score_key": has_score,
        "dict_keys": all_keys,
        "dict_values": all_values
    }


def execute_all_dir_dict_methods(initial_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Executes ALL 11 built-in public methods from dir(dict): clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, values."""
    if not isinstance(initial_dict, dict):
        raise TypeError("Input must be a dictionary")

    # 1. copy
    d = initial_dict.copy()
    
    # 2. get and setdefault
    val_name = d.get("name", "Unknown")
    role_val = d.setdefault("role", "Developer")
    
    # 3. keys, values, items
    dict_keys = list(d.keys())
    dict_vals = [str(v) for v in d.values()]
    dict_items = list(d.items())
    
    # 4. update, pop, popitem
    d.update({"status": "active", "version": "3.13"})
    popped_val = d.pop("version", None)
    popped_item = d.popitem() if d else None
    
    # 5. fromkeys
    new_from_keys = dict.fromkeys(["a", "b", "c"], 0)

    # 6. clear
    clear_demo = d.copy()
    clear_demo.clear()

    return {
        "dir_dict_methods_count": len([m for m in dir(dict) if not m.startswith("_")]),
        "modified_dict": d,
        "get_name": val_name,
        "setdefault_role": role_val,
        "dict_keys": dict_keys,
        "dict_vals": dict_vals,
        "dict_items": [str(item) for item in dict_items],
        "popped_version": popped_val,
        "popped_item": popped_item,
        "fromkeys_dict": new_from_keys,
        "cleared_dict_len": len(clear_demo)
    }


def dict_standard_libraries_and_json(pairs: List[Tuple[str, Any]]) -> Dict[str, Any]:
    """Integrates collections (defaultdict, OrderedDict, ChainMap), dictionary unpacking (**), and json serialization."""
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list of tuples")

    # 1. defaultdict
    dd = collections.defaultdict(list)
    for k, v in pairs:
        dd[k].append(v)

    # 2. OrderedDict
    od = collections.OrderedDict(pairs)
    od.move_to_end(pairs[0][0]) if pairs else None

    # 3. ChainMap
    dict1 = {"theme": "dark", "font": "Inter"}
    dict2 = {"font": "Roboto", "language": "Python"}
    cm = collections.ChainMap(dict1, dict2)

    # 4. Dict Unpacking (**)
    merged_dict = {**dict1, **dict2, "status": "merged"}

    # 5. JSON serialization
    json_str = json.dumps(merged_dict, sort_keys=True)
    parsed_json = json.loads(json_str)

    return {
        "defaultdict_result": dict(dd),
        "ordereddict_result": dict(od),
        "chainmap_font": cm["font"],
        "chainmap_language": cm["language"],
        "merged_unpacking": merged_dict,
        "json_serialized": json_str,
        "json_parsed": parsed_json
    }


def process_dict_with_standard_libraries(scores: Dict[str, int], text: str) -> Dict[str, Any]:
    """Demonstrates standard libraries working with dictionaries: types.MappingProxyType, collections.Counter, operator.itemgetter, json, sys."""
    if not isinstance(scores, dict) or not isinstance(text, str):
        raise TypeError("Invalid inputs for dict standard libraries process")

    # 1. types.MappingProxyType (read-only view)
    read_only_proxy = types.MappingProxyType(scores)
    is_read_only = True
    try:
        read_only_proxy["hacked"] = 999  # type: ignore
        is_read_only = False
    except TypeError:
        is_read_only = True

    # 2. collections.Counter dict subclass
    char_freq = collections.Counter(text)

    # 3. operator.itemgetter sorting dict by values
    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True) if scores else []

    # 4. json pretty printing (indent=2)
    pretty_json = json.dumps({"scores": scores, "top_char": char_freq.most_common(1)}, indent=2)

    # 5. sys.getsizeof benchmark
    dict_memory = sys.getsizeof(scores)

    return {
        "read_only_proxy_value": read_only_proxy.get(next(iter(scores.keys()), ""), None),
        "is_read_only_enforced": is_read_only,
        "counter_most_common": char_freq.most_common(2),
        "sorted_by_value": sorted_scores,
        "pretty_json_length": len(pretty_json),
        "dict_memory_bytes": dict_memory
    }
