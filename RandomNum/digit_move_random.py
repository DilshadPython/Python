import random


def move_random(num):
	x, y = 0, 0

	for x in range(num):		#Notrhn    South	East    West
		(dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
		x += dx
		y += dy

	return(x, y)

for x in range(40):
	# we setup the move 7 steps to each direction
	move = move_random(7)
	print(move, 'Distance from starting point = ', abs(move[0]) + abs(move[1]))

