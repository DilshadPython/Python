cities = []

with open('names.csv') as csvfile:
    for line in csvfile:
        city, county = line.rstrip().split(',')
        # we adding the data from the csvfile to the empty list
        cities.append(f"{city},{county}")

for city in sorted(cities):
    print(city)
