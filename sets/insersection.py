"""
Demonstrates intersection, difference, and union set operations on drink menus.
"""

def demo_drink_sets():
    drinks_top = {'Beer', 'Milk', 'Whiskey', 'Vodka', 'Beer', 'Whiskey', 'Rum', 'Cider', 'Milk'}
    drinks_bottom = {'Water', 'Orange', 'Whiskey', 'Heineken', 'Wine', 'Rum', 'White Wine'}

    # Items present in both sets
    common_drinks = drinks_top.intersection(drinks_bottom)
    print('Drinks in both sets:', common_drinks)

    # Items in top menu only
    top_only = drinks_top.difference(drinks_bottom)
    print('Drinks only in top menu:', top_only)

    # All unique drinks combined
    all_drinks = drinks_top.union(drinks_bottom)
    print('All unique drinks combined:', all_drinks)

    return common_drinks, top_only, all_drinks

if __name__ == '__main__':
    demo_drink_sets()
