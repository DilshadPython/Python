
def take_city(number, new_list):
	# Creat empty list
	right_list = []
	for x in range(0, number):
		right_list.append(new_list[x])
	return right_list


def drop_city(number, new_list):
	right_list = []
	for y in range(number, len(new_list)):
		right_list.append(new_list[y])
	return right_list

cietes = ["London", "Berlin", "New Yourk", "Paris", 'Rome', 'Oslo', ['a', 'b']]

pick_cities = take_city(3, cietes)

print(pick_cities)

print('Drop cities\n')

drop_cities = drop_city(3, cietes)
print(drop_cities)