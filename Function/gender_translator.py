"""
Demonstrates gender code translation function with default parameter handling.
"""
from typing import Optional


def translate_gender_code(sex: Optional[str] = None) -> str:
    """Translate gender character code ('m'/'f') to descriptive string."""
    if sex == 'm':
        return 'Male'
    elif sex == 'f':
        return 'Female'
    elif sex is None:
        return 'None'
    else:
        return 'Not in the list'


if __name__ == '__main__':
    print("Gender 'm':", translate_gender_code('m'))
    print("Gender 'f':", translate_gender_code('f'))
    print("Gender None:", translate_gender_code(None))
