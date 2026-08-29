"""
Demonstrates gender mapping with equality comparison and empty input check.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Optional


def get_gender(sex: Optional[str] = None) -> str:
    """Return standardized gender text based on input string."""
    if sex == 'm':
        return 'Male'
    elif sex == 'f':
        return 'Female'
    elif sex is None:
        return 'There is no gender'
    else:
        return 'Not in the list above'


if __name__ == '__main__':
    print("Input 'm':", get_gender('m'))
    print("Input 'f':", get_gender('f'))
    print("Input None:", get_gender())
