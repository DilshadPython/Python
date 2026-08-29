"""
Demonstrates advanced usage of *args and **kwargs in Python functions with explicit comparison.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Any, Dict, List, Tuple


def compare_args_and_kwargs(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    """
    Process and compare variable positional arguments (*args) and variable keyword arguments (**kwargs).
    
    *args captures non-keyword positional arguments as an immutable tuple.
    **kwargs captures keyword arguments (key=value pairs) as a mutable dictionary.
    
    Args:
        *args (Any): Variable positional argument inputs.
        **kwargs (Any): Variable keyword argument inputs.
        
    Returns:
        Dict[str, Any]: Comprehensive analysis dictionary comparing *args and **kwargs.
    """
    # 1. *args Processing (Positional Arguments)
    # *args collects non-keyword arguments into an ordered, immutable tuple.
    args_tuple: Tuple[Any, ...] = args
    args_list: List[Any] = list(args)
    args_count: int = len(args)
    args_type: str = type(args).__name__  # Always 'tuple'

    # 2. **kwargs Processing (Keyword Arguments)
    # **kwargs collects key=value argument pairs into a key-mapped dictionary.
    kwargs_dict: Dict[str, Any] = dict(kwargs)
    kwargs_count: int = len(kwargs)
    kwargs_type: str = type(kwargs).__name__  # Always 'dict'

    # 3. Structural Comparison Matrix
    comparison_result: Dict[str, Any] = {
        "args_summary": {
            "type": args_type,
            "count": args_count,
            "raw_tuple": args_tuple,
            "values_list": args_list,
            "description": "Positional arguments stored sequentially in an immutable tuple."
        },
        "kwargs_summary": {
            "type": kwargs_type,
            "count": kwargs_count,
            "values_dict": kwargs_dict,
            "keys": list(kwargs_dict.keys()),
            "description": "Keyword arguments stored as key-value mappings in a dictionary."
        },
        "is_args_empty": args_count == 0,
        "is_kwargs_empty": kwargs_count == 0
    }

    return comparison_result


if __name__ == '__main__':
    result = compare_args_and_kwargs(10, "Python", 3.13, user="John", role="Developer", status="Active")
    print("=== *args vs **kwargs Comparison Analysis ===")
    print("Positional (*args):", result["args_summary"])
    print("Keyword (**kwargs):", result["kwargs_summary"])
