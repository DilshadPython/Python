"""
Demonstrates set attribute inspection and adding heterogeneous elements.
"""

def demo_set_info():
    test_set = set()
    test_set.add(17)
    test_set.add(False)
    test_set.add('Hello world')

    print('Populated test set:', test_set)
    has_17 = 17 in test_set

    return test_set, has_17

if __name__ == '__main__':
    demo_set_info()
