from collections import Counter


cieties = ['Paris', 'Berlin', 'Stockholm', 'Roma', 'London', 'Tokyo', 'Berlin', 'Paris', 'Roma', 'Stockholm', 'Berlin']

numbers = Counter(cieties)

position = Counter(numbers)

print(numbers)
# print(position['Roma'])