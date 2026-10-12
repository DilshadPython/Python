"""
Demonstrates character list reversal and sorting.
"""

def demo_char_list():
    char_list = ['s', 'i', 'p', 'k', 'a', 'g', 'o', 'd']
    print('Original character list:', char_list)

    char_list.reverse()
    print('Reversed character list:', char_list)

    char_list.sort()
    print('Sorted character list:', char_list)

    return char_list

if __name__ == '__main__':
    demo_char_list()
