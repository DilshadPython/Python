"""
Demonstrates conditional evaluation and filtering on numeric lists.
"""

def demo_numeric_filter():
    nums = [74, 91, 53, 2, 70, 36, 5, 55, 31, 54]

    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]

    print('Even numbers:', evens)
    print('Odd numbers:', odds)

    return evens, odds

if __name__ == '__main__':
    demo_numeric_filter()
