cities = []

with open('names.csv') as csvfile:
    for line in csvfile:
        city, county = line.rstrip().split(',')
        name = {'city': city, 'county': county}
        cities.append(name)

# we are sorting the city which is the key using lamda function unknowon function
for name in sorted(cities, key=lambda name: name['city']):
    print(f'{name["city"]},{name["county"]}')