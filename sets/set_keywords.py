"""
Demonstrates set algebraic operations: intersection, difference, union.
"""

def demo_set_algebra():
    language_1 = {'Python', 'Java', 'PHP', 'JavaScript'}
    language_2 = {'Java', 'C++', 'PHP', '.Net', 'C#'}

    common = language_1.intersection(language_2)
    only_in_1 = language_1.difference(language_2)
    only_in_2 = language_2.difference(language_1)
    all_langs = language_1.union(language_2)

    print('Common languages:', common)
    print('Only in set 1:', only_in_1)
    print('Only in set 2:', only_in_2)
    print('All languages:', all_langs)

    return common, only_in_1, only_in_2, all_langs

if __name__ == '__main__':
    demo_set_algebra()
