#  What we try to achive here is to collecte the data but not the duplecate

drinks_top = {'Beer', 'Milk', 'Whiskey', 'Vodka',
              'Beer', 'Whiskey', 'Rum', 'Cider', 'Milk'}

drinks_bottom = {'Water', 'Orange', 'Whiskey',
                 'Heinken', 'Wine', 'Rum', 'White Wine'}


print('\n - Display the drinks are available in both. \n')
print(drinks_top.intersection(drinks_bottom))

print('\n - Display the drinks are not available in both. \n')
print(drinks_top.difference(drinks_bottom))

print('\n - Add the two set together. \n')
print(drinks_top.union(drinks_bottom))

print('\n - Create empty list tuple and set')

print('\n Empty list. \n')
empty_list = []
empty_list = list()
print(empty_list)

print('\n - Empty tuple.\n')
empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple)

print('\n Empty Set. \n')
empty_set = {}
print(empty_set, ' <<< This is dictionary not Set!!!')

empty_set = set()
print(empty_set)
