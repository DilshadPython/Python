"""
Demonstrates sorting dictionaries by value using lambda functions.
"""

def demo_sort_dict_by_value():
    numbers = {
        'a': 9, 'b': 3, 'c': 4, 'd': 6, 'e': 0,
        'f': 11, 'g': 23, 'h': -8, 'i': 27, 'j': 15
    }

    print('Original dict:', numbers)

    # Sort by value ascending using lambda
    sorted_by_val_asc = sorted(numbers.items(), key=lambda item: item[1])
    print('Sorted by value (ascending):', sorted_by_val_asc)

    # Sort by value descending using lambda
    sorted_by_val_desc = sorted(numbers.items(), key=lambda item: item[1], reverse=True)
    print('Sorted by value (descending):', sorted_by_val_desc)

    return sorted_by_val_asc, sorted_by_val_desc

if __name__ == '__main__':
    demo_sort_dict_by_value()
