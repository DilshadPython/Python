"""
Demonstrates string formatting and sorting using Python lambda functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Callable, List

# Lambda function to format full name with title capitalization and space stripping
format_full_name: Callable[[str, str], str] = lambda fname, lname: f"{fname.strip().title()} {lname.strip().title()}"


def sort_names_by_last_name(name_list: List[str]) -> List[str]:
    """
    Sort a list of full names alphabetically by last name using a lambda key function.
    
    Args:
        name_list (List[str]): List of full name strings.
        
    Returns:
        List[str]: New list of names sorted by last name.
    """
    sorted_list: List[str] = list(name_list)
    sorted_list.sort(key=lambda name: name.split(' ')[-1].lower())
    return sorted_list


if __name__ == '__main__':
    print("Formatted Name:", format_full_name(" john", "  smith"))

    sample_names: List[str] = [
        'John Smith',
        'Nicholas Herriot',
        'Paulo Maldini',
        'Chris Ederson',
        'Steven Case'
    ]
    print("Original Names:", sample_names)
    print("Sorted by Last Name:", sort_names_by_last_name(sample_names))
