import random


def random_move(num):
	x, y = 0, 0

	for x in range(num):		#Notrhn    South	East    West
		(dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
		x += dx
		y += dy
	return(x, y)


number_of_steps = 11001

for move_length in range(1, 37):
	# we setup the move 7 steps to each direction
	none_transport = 0

	for x in range(number_of_steps):
		(x, y) = random_move(move_length)
		distance = abs(x) + abs(y)

		if distance <= 4:
			none_transport += 1

	no_transport_percentage = float(none_transport) / number_of_steps
	print('Move size = ', move_length, " / %  of no transport = ", 100 * no_transport_percentage)
