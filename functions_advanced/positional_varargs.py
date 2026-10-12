"""
Demonstrates positional variable-length argument list (*args) handling in Python functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Any, Tuple


def process_positional_args(heading: Any, *args: Any) -> Tuple[Any, Tuple[Any, ...]]:
    """
    Process required heading parameter and arbitrary positional arguments (*args).
    
    Args:
        heading (Any): Primary required argument identifier.
        *args (Any): Variable length tuple of positional arguments.
        
    Returns:
        Tuple[Any, Tuple[Any, ...]]: Tuple containing heading and args tuple.
    """
    print(f"Start testing format of heading: {heading}")
    for item in args:
        print(f"Positional arg: {item}")
    return heading, args


if __name__ == '__main__':
    hdr, arguments = process_positional_args(2, 9, 3)
    print("Returned heading:", hdr)
    print("Returned positional arguments:", arguments)
