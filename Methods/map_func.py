import math


def sqr_area(radius):
	''' Calculate area of a circle with radius '''
	rad = math.pi * (radius**2)
	return rad

# we  have a list of circle
radi = [6.5, 3.1, 0.7, 0.51, 22.3]

# we create an empty list
empty_area = []

# we go throw the list using the sqr_area function
for r in radi:
	a = sqr_area(r)
	empty_area.append(a)

print(empty_area)
print()
# Now we use map function does all in one line, how it works:
''' The map function will take 2 argument first is a function second is a list or tuple or other itrable 
object
''' 
new_way = map(sqr_area, radi)
print(new_way)

print()
new_way_update = list(map(sqr_area, radi))
print(new_way_update)

