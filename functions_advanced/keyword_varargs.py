"""
Demonstrates keyword variable-length argument list (**kwargs) handling in Python functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Any, Dict, Tuple


def process_keyword_args(word: Any, **kwargs: Any) -> Tuple[Any, Dict[str, Any]]:
    """
    Process required word argument and arbitrary keyword arguments (**kwargs).
    
    Args:
        word (Any): Primary required word argument.
        **kwargs (Any): Variable length dictionary of keyword arguments.
        
    Returns:
        Tuple[Any, Dict[str, Any]]: Tuple containing word and kwargs dictionary.
    """
    print(f"Start test word: {word}")
    for key, value in kwargs.items():
        print(f"Key-value pair: {key} = {value}")
    return word, kwargs


if __name__ == '__main__':
    w_val, kw_dict = process_keyword_args(word=8, myword="Hello", keyword_val=27)
    print("Returned word:", w_val)
    print("Returned kwargs:", kw_dict)
