"""
Demonstrates duplicate elimination and set union / intersection operations.
"""

def demo_set_duplicates():
    fruits = {'apples', 'oranges', 'cherry', 'bananas', 2.7}
    numbers = {21, 9, 2.7, -5, 'oranges'}

    # union returns all unique items across both sets
    union_set = fruits.union(numbers)
    print('Union of fruits and numbers:', union_set)

    # intersection returns common elements
    intersection_set = fruits.intersection(numbers)
    print('Intersection:', intersection_set)

    # difference returns items in first set but not second
    first = {'Hello', 22, 'Python', 'Java', 7, 9, True}
    second = {9, 'Java', 22, True, 'Python', 'JavaScript', False}
    diff_set = first.difference(second)
    print('Difference (first - second):', diff_set)

    return union_set, intersection_set, diff_set

if __name__ == '__main__':
    demo_set_duplicates()
