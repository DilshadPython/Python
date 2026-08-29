"""
Demonstrates gender code translation function with default parameter handling.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Optional


def get_gender(sex: Optional[str] = None) -> str:
    """Translate gender character code to descriptive string."""
    if sex == 'm':
        return 'Male'
    elif sex == 'f':
        return 'Female'
    elif sex is None:
        return 'None'
    else:
        return 'Not in the list'


if __name__ == '__main__':
    print("Gender 'm':", get_gender('m'))
    print("Gender 'f':", get_gender('f'))
    print("Gender None:", get_gender(None))
