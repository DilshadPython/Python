
# How to sort a Python dict by value

text = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}

# two way to do it
first = sorted(text.items(), key=lambda x: x[1])
print('First: ', first)

# second way
import operator
second = sorted(text.items(), key=operator.itemgetter(1))

print('')
print('Second: ', second)
