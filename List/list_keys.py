names = ['Dilshad', 'Azad']

print(dir(names))
"""
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
 '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

"""
# You can't use split() in List

print('\n Before adding new name : >> ', names)
names.append('Barbara')
print('\n Adding another name : >> ', names)

names.sort()
print('\n Sorted the list: ', names)

sorted_name = sorted(names)
print('\n We can sorted another way: ', sorted_name)

names.reverse()
print('\n Revered the list: ', names)

names.insert(0, 'Baxan')
print('\n We adding another name at the fest index in the list: ', names)

print('\n We display the index(2) of list: ', names[2])

print('\n We display the index place of specific name in the list: ', names.index('Azad'))

new_name = ['Alex', 'Talar', 'Tarza']
names.extend(new_name)
print('\n We Extend the list: ', names)

new_name = ['Lanja', 'Anja', 'Ario']
names.append(new_name)
print('\n We Apped the list: ', names)

names.remove('Alex')
print('\n We Remove a specific name in the list: ', names)

names.pop()
print('\n We Remove the last name in the list if we not put any args: ', names)

removed = names.pop()
print('Removed name is >> ', removed)
print('\n We will show the removed name in the list : ', names)

names.sort(reverse=True)
print('\n We reversed another way: ', names)

print('\n Search if the name not exist in the list: ', 'Shkar' in names)
print('\n Search if the name exist in the list: ', 'Azad' in names)

names.clear()
print('\n We try to clear the list like be empty: >>> ', names)

