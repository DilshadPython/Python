"""
Demonstrates basic list creation, length evaluation, and element access.
"""

def demo_basic():
    sample_list = ['python', 3.12, True, [1, 2]]
    print('Sample list:', sample_list)
    print('Length of list:', len(sample_list))
    print('First element:', sample_list[0])
    print('Last element:', sample_list[-1])

    return sample_list

if __name__ == '__main__':
    demo_basic()
