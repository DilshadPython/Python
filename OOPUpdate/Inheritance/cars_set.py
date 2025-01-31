cars = [
    {'name': 'Audi', 'model': 'A7', 'year': 2024},
    {'name': 'BMW', 'model': 'M60', 'year': 2011},
    {'name': 'Mercedes', 'model': 'AMG CLC', 'year': 2025},
    {'name': 'WV', 'model': 'Golf 5', 'year': 2020},
    {'name': 'Audi', 'model': 'A5', 'year': 2022},
    {'name': 'BMW', 'model': 'iX2', 'year': 2024},
    {'name': 'BMW', 'model': 'iX3', 'year': 2020},
    {'name': 'Audi', 'model': 'Q5', 'year': 2011},
    {'name': 'WV', 'model': 'Polo', 'year': 2010},
    {'name': 'Mercedes', 'model': 'AMG 4x4', 'year': 2010},
    {'name': 'Volvo', 'model': 'XV 4x4', 'year': 2012},
    {'name': 'Audi', 'model': 'Q8', 'year': 2015},
    {'name': 'Audi', 'model': 'Q3', 'year': 2023},
]

# we creat an empty list and we add all the name and models including years
# to the list but we use set method to remove all duplicate name, model and year
# cars = {}
names = set()
models = set()
years = set()

for car in cars:
    if car['name'] not in names:
        names.append(car['name'])
    if car['model'] not in models:
        models.append(car['model'])
    if car['year'] not in years:
        years.append(car['year'])

# all in one for loop
for (name, model, year) in zip(names, models, years):
    print(name, ' ', model, ' ', year)

# Names only
print('\n####################################')
for name in names:
    print(name)

print('\n####################################')
for model in models:
    print(model)

print('\n####################################')
for year in years:
    print(year)