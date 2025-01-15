import random

cars = ['BMW', 'Tesla', 'Mercedes', 'Ford', 'Audi', 'Volkswagen', 'Ferrari', 'Volvo']

print('Display the cars as in the list')
for car in cars:
    print(car)

car_shuffled = cars[::-1]
print('\nDisplay from right to left')
print(car_shuffled)

print('\n')

random.shuffle(cars)

print('Display the cars shuffled from the list')
for car in cars:
    print(car)


