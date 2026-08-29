"""
Demonstrates list concatenation using '+' and '+=' operators.
"""

def demo_concatenation():
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]

    # Plus operator creates a new combined list
    combined = list_a + list_b
    print('Combined with +:', combined)

    # Plus-equals operator extends list_a in-place
    list_a += list_b
    print('List A after += list_b:', list_a)

    return combined, list_a

if __name__ == '__main__':
    demo_concatenation()
