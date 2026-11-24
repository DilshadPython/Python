"""
Demonstrates tuple index lookup and count methods.
"""

def demo_tuple_lookup():
    tup = ('England', 24, 'USA', 'France', 24, 'Germany', 'Spain', 24, -10, 'Italy', 16, 24)

    idx_france = tup.index('France')
    idx_spain = tup.index('Spain')
    idx_neg = tup.index(-10)

    count_24 = tup.count(24)
    count_france = tup.count('France')

    print('France index:', idx_france)
    print('Spain index:', idx_spain)
    print('-10 index:', idx_neg)
    print('Count of 24:', count_24)

    return idx_france, count_24

if __name__ == '__main__':
    demo_tuple_lookup()
