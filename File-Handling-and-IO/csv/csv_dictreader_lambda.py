# using csv library
import csv

cities = []

with open('multynames.csv') as csvfile:
   reader = csv.DictReader(csvfile)
   # for row in reader:
   #     cities.append({'city': row[0], 'county': row[1]})
   for row in reader:
       cities.append({'city': row['city'], 'county': row['county'], 'country': row['country']})

# we are sorting the city which is the key using lamda function unknowon function
for name in sorted(cities, key=lambda name: name['city']):
    print(f'{name["city"]} is in {name["county"]} - {name["country"]}')
