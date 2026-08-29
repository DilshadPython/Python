"""
Demonstrates using filter(None, iterable) to strip empty, falsy, or null values.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Any, List


def remove_falsy_values(items: List[Any]) -> List[Any]:
    """
    Filter out all falsy values (0, '', None, False, [], {}, ()) from a sequence.
    
    Args:
        items (List[Any]): Input sequence containing mixed elements.
        
    Returns:
        List[Any]: Filtered list containing only truthy elements.
    """
    return list(filter(None, items))


if __name__ == '__main__':
    capitals: List[Any] = [
        'Rome',
        '',
        'Paris',
        'Berlin',
        '',
        False,
        '',
        None,
        'London',
        'Stockholm',
        'Amsterdam',
        '',
        0.0,
        'Cairo',
        '',
        {},
        '',
        'Erbil',
        0,
        'New York',
        [],
        {0: 0}
    ]
    print("Original items count:", len(capitals))
    filtered = remove_falsy_values(capitals)
    print("Filtered truthy items:", filtered)
    print("Filtered items count:", len(filtered))
