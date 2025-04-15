
for (x, y) in enumerate(["London", "Berlin", "New Yourk", "Paris", 'Rome', 'Oslo', ['a', 'b']]):
    print(x, y)
print('\n------\n')
cities = ["London", "Berlin", "New Yourk", "Paris", 'Rome', 'Oslo']

for index, city in enumerate(cities):
    print(index, city)
print('\n------\n')
for index, city in enumerate(cities, start=1):
    print(index, city)