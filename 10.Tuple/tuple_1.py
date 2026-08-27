"""
Demonstrates basic tuple creation, empty tuples, and heterogeneous elements.
"""

def demo_tuple_basics():
    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5)
    tup3 = ('a', 'b', 'c', 'd')
    tup4 = ()

    print('tup1:', tup1)
    print('tup2:', tup2)
    print('tup3:', tup3)
    print('tup4:', tup4)

    return tup1, tup2, tup3, tup4

if __name__ == '__main__':
    demo_tuple_basics()
