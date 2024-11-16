# Iterator is read the num or string in the list but when we called with next 
# it read only one index but if called more than go to next is like for loop
# but manualy see the example below

numbers = [1, 2, 3, 4, 5,]

# we make the list iterable
itr = iter(numbers)

print(itr.__next__())

print('*******************')
names = ['Paris', 'London', 'Berlin', 'Tokyo', 'Roma']

name = iter(names)
print(name.__next__())
print(name.__next__())
print(name.__next__())
print(name.__next__())
print(name.__next__())

print('#####################')

cars = ['Audi', 'Fiat', 'Alfa Romie', 'Porsh', 'Volvo']

car = iter(cars)
print(next(car))
print(next(car))
print(next(car))