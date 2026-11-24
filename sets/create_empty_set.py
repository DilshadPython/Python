"""
Demonstrates set instantiation rules vs dictionary creation.
"""

def demo_empty_instantiations():
    # CRITICAL: {} creates an empty dictionary, NOT an empty set!
    empty_dict = {}
    dict_type = type(empty_dict)

    # Correct way to instantiate empty set: set()
    empty_set = set()
    set_type = type(empty_set)

    empty_list = list()
    empty_tuple = tuple()

    print('{} type:', dict_type)
    print('set() type:', set_type)

    return dict_type, set_type

if __name__ == '__main__':
    demo_empty_instantiations()
