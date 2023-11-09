cietes = ["London", "Berlin", "New Yourk", "Paris", 'Rome', 'Oslo', ['a', 'b']]

def take_city(number, new_list):
	# Creat empty list
	right_list = []
	for x in range(-7, -4):
		right_list.append(new_list[x])
	return right_list


def drop_city(number, new_list):
	right_list = []
	for y in range(-4, 0):
		right_list.append(new_list[y])
	return right_list


pick_cities = take_city(3, cietes)

print(pick_cities)

print('Drop cities\n')

drop_cities = drop_city(3, cietes)
print(drop_cities)