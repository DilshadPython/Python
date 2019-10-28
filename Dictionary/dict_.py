# How we sort python dict by value?

numbers = {
    'a': 9,
    'b': 3,
    'c': 4,
    'd': 6,
    'e': 0,
    'f': 11,
    'g': 23,
    'h': -8,
    'i': 27,
    'j': 15
}

print(numbers)
print()
print()

print(' First we will use lamda function to dort the dictionary from small to highest number.')
print('1. We will sorteded the dictionary from smallest number to highest: ')
print('##' * 35)
sort_num = sorted(numbers.items(), key=lambda i: i[1])
print(sort_num)
print()
print()


print('##' * 35)
print(' In the second way we will use 2 function with for loop, sorted() items() and for.')
print('2. Using for loop with items() to sort dictionary: ')
# for key, value in sorted(numbers.iteritems()): # python2
for key, value in sorted(numbers.items()):  # python3
    print(key, ' > ', value)

print()
print()
print('Here in the third option we will import operator from python lib and use 3 methods or function,\
    sorted(), items() and itemgetter().')
print('3. Using operator to sort the dictionary:')
print('##' * 35)
import operator
opr = sorted(numbers.items(), key=operator.itemgetter(1))

print(opr)

print()
print()
names = {'1': 'Milk', '2': 'Bread',
         '3': 'Cheese', '4': 'Vegitable', '5': '7Up'}

print('In the fourt way we will use lambda methd with sorted() and items() methods to sorted alphabetically.')
print('4. We will sorteded the dictionary alphabetically: ')
print('##' * 35)
sort_names = sorted(names.items(), key=lambda x: x[1] + '\n')

print(sort_names)
