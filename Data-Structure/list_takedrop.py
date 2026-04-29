cities = [55, "London", "Berlin", ['a', 'b', 3, 4], "New Yourk", "Paris", 'Rome', 'Oslo' ]
print('City list: ', cities)

def take_city(number, new_list):
	# Creat empty list
	right_list = []
	number = int(input('Enter the number of above cities you want to keep it: '))
	for x in range(0, number):
		right_list.append(new_list[x])
	return right_list

pick_cities = take_city(4, cities)

print('\nPick first  cities: ', pick_cities)

print('\t======' * 12)

print('City list: ', cities)

number = int(input('Enter the number of cities above you want to drop it: '))
def drop_city(number, new_list):
	right_list = []
	for y in range(number, len(new_list)):
		right_list.append(new_list[y])
	return right_list

drop_cities = drop_city(number, cities)
print('\nDrop cities: ', drop_cities)