"""
Demonstrates built-in tuple methods (.count(), .index()) and immutability.
"""

def demo_builtin_tuple():
    # Empty tuple constructor
    empty_tuple = tuple()

    # Public methods on tuple object
    methods = [m for m in dir(empty_tuple) if not m.startswith('_')]
    print('Public methods on tuple:', methods)

    nums = (3, 7, 11, 6, 3, 17, 11, 23, 0, 9, 11)
    print('Numbers tuple:', nums)

    # Immutability verification: nums[0] = 2 raises TypeError
    count_11 = nums.count(11)
    index_17 = nums.index(17)

    print('Count of 11:', count_11)
    print('Index of 17:', index_17)

    return methods, count_11, index_17

if __name__ == '__main__':
    demo_builtin_tuple()
