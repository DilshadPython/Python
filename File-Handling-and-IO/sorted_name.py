cities = []

with open('cities.txt') as f:
    # reading the name from the file and appended in the empty list
    for line in f:
        cities.append(line.rstrip())

# now we are sorting the names in the list
for city in sorted(cities):
    print(f'Hi, {city}')