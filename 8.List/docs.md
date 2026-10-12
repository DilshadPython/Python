List:
Ordered, mutable, with duplicates

# Add the item to the end of the list you can use also for add another list inside the list you want list inside list_a
.append()

.copy()
.count()
.min()
.max()
.sum()

# Return the index number and the item
enumerate()
>>> chars = ['a', 'b', 'c', 'd']
>>> for index, char in enumerate(chars):
...     print(index, char)
... 
0 a
1 b
2 c
3 d
> 
for index, char in enumerate(chars, start=1):
...     print(index, char)
... 
1 a
2 b
3 c
4 d

# .join() 
split_by = '; '.join(chars)
>>> print(split_by)
a; b; c; d
split_by = ' || '.join(chars)
>>> print(split_by)
a || b || c || d

new_chars = split_by.split(' || ')
>>> print(new_chars)
['a', 'b', 'c', 'd']



# find the path index of char
chars = ['a', 'b', 'c', 'd']
>>> path = chars.index('c')
>>> print(path)
2

.index()

# in How we use in the list
in 
>>> course = ['Math', 'Chemics', 'Media', 'Physics']
> >>> print('Media' in course)
True


# add the item to specific index and use 2 args insert(index, 'item')
.insert()
# >>> chars = ['a', 'b', 'c', 'd']
>>> chars.reverse()
>>> print(chars)
['d', 'c', 'b', 'a']
.reverse()
 

# Remove the item you want like chars.remove('b')
chars = ['a', 'b', 'c', 'd']
>>> print(chars)
['a', 'b', 'c', 'd']
chars.remove('b')
>>> print(chars)
['a', 'c', 'd']
.remove()

# Sort alphabetic or as numbers from less to more
works = ['Developer', 'Electric', 'Plumber', 'Firework']
>>> works.sort()
>>> print(works)
['Developer', 'Electric', 'Firework', 'Plumber']
> works.sort(reverse=True)
print(works)
['Developer', 'Electric', 'Firework', 'Plumber']
>>> works.sort(reverse=True)
>>> print(works)
['Plumber', 'Firework', 'Electric', 'Developer']
>>> works.sort(reverse=False)
>>> print(works)
['Developer', 'Electric', 'Firework', 'Plumber']
.sort()
> course = ['Math', 'chemics', 'Media', 'Physics']
> sorted(course)
['Math', 'Media', 'Physics', 'chemics']
course = ['Math', 'Chemics', 'Media', 'Physics']
>>> now_sorted = sorted(course)
>>> print(now_sorted)
['Chemics', 'Math', 'Media', 'Physics']

# This remove the last item in the end of the list, example chars = ['a', 'b', 'c'] delete c without enter any item
chars = ['a', 'b', 'c', 'd']
chars.pop()
'd'
>>> print(chars)
['a', 'c']
ew_l = chars.pop()
>>> 
>>> print(new_l)
c
>>> print(chars)
['a']
.pop()
>>> chars = ['a', 'b', 'c', 'd']
>>> print(chars.pop())
d
>>> my_l = chars.pop()
>>> print(my_l)
c
>>> print(chars)
['a', 'b']

# Add two list together list_1, list_2 used like that list_1.extend(list_2) 
.extend()
.index()
.clear()