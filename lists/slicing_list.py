"""
Comprehensive demonstration of Python list slicing syntax [start:stop:step].
"""

def demo_slicing():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Original numbers:', num)

    slice_first_five = num[:5]
    slice_from_index_three = num[3:]
    slice_middle = num[2:7]
    slice_negative_indices = num[-6:-2]
    slice_with_step = num[1:-2:2]
    slice_reversed = num[::-1]

    print('First 5 [:5]:', slice_first_five)
    print('From index 3 [3:]:', slice_from_index_three)
    print('Middle range [2:7]:', slice_middle)
    print('Negative indices [-6:-2]:', slice_negative_indices)
    print('Step slicing [1:-2:2]:', slice_with_step)
    print('Reversed sequence [::-1]:', slice_reversed)

    return slice_first_five, slice_reversed

if __name__ == '__main__':
    demo_slicing()
