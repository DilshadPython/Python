languge_1 = {'Python', 'Java', 'PHP', 'JavaScript'}
languge_2 = {'Java', 'C++', 'PHP', '.Net', 'C#'}

print('\n Use intersection to display duplicated languages are in both sets.')
print(languge_1.intersection(languge_2))

print('\n Use difference to display which languages are new in the second set.')
print(languge_1.difference(languge_2))

print('\n Use difference to display which languages are new in the first set.')
print(languge_2.difference(languge_1))

print('\n Use union to display all languages are in both sets with no duplication.')
print(languge_1.union(languge_2))

print()
print(dir(languge_1))