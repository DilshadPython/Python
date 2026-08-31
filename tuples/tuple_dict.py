"""
Demonstrates dict.items() tuple pairs and lexicographical comparison of tuples.
"""

def demo_tuple_comparison():
    my_dict = {'Hello': 7, 'Python': 9}

    items_tuples = list(my_dict.items())
    print('dict.items() tuples:', items_tuples)

    # Lexicographical comparison of tuples
    comp1 = (0, 3, 7) < (1, 3, 7)  # True (0 < 1)
    comp2 = (0, 3, 17) < (0, 3, 7) # False (17 not < 7)

    print('(0, 3, 7) < (1, 3, 7):', comp1)
    print('(0, 3, 17) < (0, 3, 7):', comp2)

    return items_tuples, comp1, comp2

if __name__ == '__main__':
    demo_tuple_comparison()
