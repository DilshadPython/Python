cities = []

with open('names.csv') as csvfile:
    for line in csvfile:
        city, county = line.rstrip().split(',')
        name = {}
        name['city'] = city
        name['county'] = county
        cities.append(name)

for name in cities:
    # print(name)
    print(f"{name['city']}, in {name['county']}")
