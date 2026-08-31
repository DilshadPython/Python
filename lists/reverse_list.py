"""
Demonstrates in-place sorting and reversing using sort() and reverse() methods.
"""

def demo_reversing():
    # Fixed spelling: Vegetable
    foods = ['Milk', 'Bread', 'Cheese', 'Vegetable']
    print('Original foods:', foods)

    foods.sort()
    print('Sorted foods:', foods)

    foods.sort(reverse=True)
    print('Reverse sorted foods:', foods)

    teams = ['Liverpool', 'Man City', 'Chelsea', 'Tottenham']
    print('\nOriginal teams:', teams)

    teams.reverse()
    print('In-place reversed teams:', teams)

    return foods, teams

if __name__ == '__main__':
    demo_reversing()
