cities = []

with open('names.csv') as csvfile:
    for line in csvfile:
        city, county = line.rstrip().split(',')
        name = {'city': city, 'county': county}
        cities.append(name)

def get_city(name):
    return name['city']

def get_county(name):
    return name['county']

# we are sorting the city which is the key
for name in sorted(cities, key=get_city, reverse=True):
    print(f'{name["city"]},{name["county"]}')

print('###################')

# we are sorting the county which is the value
for name in sorted(cities, key=get_county, reverse=True):
    print(f'{name["city"]},{name["county"]}')