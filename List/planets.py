my_planets = [
    #   0        1     2    3
    ('Mercury', 2440, 5.43, 0.395),
    ('Venus', 6125, 5.27, 987),
    ('Earth', 6325, 5.11, 1.002),
    ('Mars', 5680, 5.13, 1.658),
    ('Jupiter', 3105, 0.49, 6.251),
    ('Saturn', 7320, 1.45, 7.365),
    ('Uranus', 2879, 0.615, 8.361),
    ('Neptune', 2440, 1.51, 33.330),
]

# we will sorted which is the largest planet

size = lambda planet: planet[1]
my_planets.sort(key=size, reverse=True)

print(my_planets)

print()
print('###' * 30)

density = lambda planet: planet[2]
my_planets.sort(key=density)

print(my_planets)

print()
print('###' * 30)

last = lambda planet: planet[3]
my_planets.sort(key=last)

print(my_planets)
