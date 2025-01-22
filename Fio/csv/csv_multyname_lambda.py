# using csv library
import csv

cities = []

with open('multynames.csv') as csvfile:
   reader = csv.reader(csvfile)
   # for row in reader:
   #     cities.append({'city': row[0], 'county': row[1]})
   for name, home in reader:
       cities.append({'name': name, 'home': home})

# we are sorting the city which is the key using lamda function unknowon function
for x in sorted(cities, key=lambda x: x['name']):
    print(f'{x["name"]} is in {x["home"]}')
