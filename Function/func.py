def create_tunnel(cave_from, cave_to):
	""" Create a tunnel between cave_from and cave_to """
	caves[cave_from].append(cave_to)
	caves[cave_to].append(cave_from)

def visit_cave(cave_number):
	""" Mark a cave as visited """
	visited_caves.append(cave_number)
	unvisited_caves.remove(cave_number)

def choose_cave(cave_list):
	""" Pick a cave from a list, provided that the cave has less than 3 tunnels."""
	cave_number = choice(cave_list)
	while len(caves[cave_number]) >= 3:
		cave_number = choice(cave_list)
	return cave_number

def print_caves():
	""" Print out the current cave structure """
	for number in cave_numbers:
		print number, ":", caves[number]
		print '----------'