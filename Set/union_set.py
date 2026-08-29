"""
Demonstrates symmetric difference and mathematical set equality.
"""

def demo_set_properties():
    blue_eyes = {'Mandy', 'Thomas', 'Sophia', 'Ebra', 'Ela', 'George'}
    blond_hair = {'Klara', 'Hemen', 'George', 'Stewart', 'Adam', 'Mandy', 'Sophia'}

    # Commutative property of union: A | B == B | A
    union_equal = (blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))

    # Commutative property of intersection: A & B == B & A
    intersect_equal = (blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))

    # Difference is NOT commutative: A - B != B - A
    diff_equal = (blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair))

    # Symmetric difference IS commutative: A ^ B == B ^ A
    sym_diff_equal = (blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair))

    print('Union commutative:', union_equal)
    print('Intersection commutative:', intersect_equal)
    print('Difference commutative:', diff_equal)
    print('Symmetric difference commutative:', sym_diff_equal)

    return union_equal, intersect_equal, diff_equal, sym_diff_equal

if __name__ == '__main__':
    demo_set_properties()
