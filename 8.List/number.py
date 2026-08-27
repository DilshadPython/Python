"""
Demonstrates sorted() function vs list.sort() method on numeric lists.
"""

def demo_sort_comparison():
    num_lst = [6, 9, 2, 3, 5, 7, 4, 10, 1, 8]

    # sorted() creates a new list, leaving original intact
    sorted_copy = sorted(num_lst)
    print('New sorted list:', sorted_copy)
    print('Original list unchanged:', num_lst)

    # num_lst.sort() sorts the original list in-place and returns None
    num_lst.sort()
    print('Original list after .sort():', num_lst)

    return sorted_copy, num_lst

if __name__ == '__main__':
    demo_sort_comparison()
