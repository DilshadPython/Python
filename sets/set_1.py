"""
Demonstrates iterating over sets and checking element membership using 'in'.
"""

def demo_set_membership():
    alcohol_set = {'Beer', 'Whiskey', 'Milk', 'Vodka', 'Beer', 'Whiskey', 'Rum', 'Cider', 'Milk'}

    print('Deduplicated beverage count:', len(alcohol_set))
    has_beer = 'Beer' in alcohol_set
    has_wine = 'Wine' in alcohol_set

    print('Is Beer in set?:', has_beer)
    print('Is Wine in set?:', has_wine)

    return has_beer, has_wine

if __name__ == '__main__':
    demo_set_membership()
