"""
Demonstrates combining positional (*args) and keyword (**kwargs) variable arguments in Python functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Any, Dict, Tuple


def print_args_details(*args: Any, **kwargs: Any) -> Tuple[Any, ...]:
    """Inspect and return positional arguments tuple."""
    print("Enter positional details:", args)
    return args


def print_kwargs_details(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    """Inspect and return keyword arguments dictionary."""
    print("Enter keyword details:", kwargs)
    return kwargs


def print_combined_user_details(*args: Any, **kwargs: Any) -> Tuple[Tuple[Any, ...], Dict[str, Any]]:
    """Inspect and return combined positional (*args) and keyword (**kwargs) argument containers."""
    print("Enter combined user details:", args, kwargs)
    return args, kwargs


if __name__ == '__main__':
    print_args_details('Dilshad', 'Abdulla', 'Developer')
    print_kwargs_details(fname='Dilshad', lname='Abdulla', height=175)
    args_tup, kwargs_dict = print_combined_user_details('Adam', 'Smith', 44, fname='Adam', country='UK')
    print("Args:", args_tup)
    print("Kwargs:", kwargs_dict)
