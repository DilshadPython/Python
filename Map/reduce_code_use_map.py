import math


def area(r):
    return math.pi * (r**2)

mylist  = [3,7, 2.1, 8, 9-3, 2.2]

# create an empty list
empty_list = []

for x in mylist:
    a = area(x)
    empty_list.append(a)

print(empty_list)

print()
# When we use map function reduce the code map function take 2 arguments the func and it's your new empty list
result = map(area, mylist)
print(result)
print()
# the output is map objects
find = list(map(area, mylist))
print(find)