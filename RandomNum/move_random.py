import random


def move_randomly(num):
    '''' Return coordinates after num block move randomly'''
    x = 0
    y = 0

    for x in range(num):
        # define direction
        steps = random.choice(['Notrh', 'South', 'East', 'West'])

        # if we going north
        if steps == 'North':
            y = y + 1
        # going south
        elif steps == 'South':
            y = y - 1
        # going east
        elif steps == 'East':
            x = x + 1
        # going west
        else:
            x = x - 1
    return (x, y)


for x in range(40):
    move = move_randomly(5)
    print(move, 'Distanc from index point = ', abs(move[0]) + abs(move[1]))
