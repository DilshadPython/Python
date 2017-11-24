
first_list = ['Milk', 'Bread', 'Cheese', 'Vegitable']

second_list = ['Bow and Arrow', 'Lantern', 'Wumpus B Gone']

print('First list: ', first_list)
print('Second list: ', second_list)
print('\n')

my_shopping_lists = [first_list, second_list]

print('My Shopping list: ', my_shopping_lists)
print('\n')

print('Added Rope to the second list')
second_list.append('Rope')
print(second_list)
print('\n')

second_list.remove('Wumpus B Gone')
print('Removed Wumpus B Gone from second list')
print(second_list)

print('\n')
print(my_shopping_lists)