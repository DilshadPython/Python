
account = {'fname': 'Dilshad', 'lname': 'Abdulla', 
			'address': '16 Glebe Road', 
			'date_of_birth': '28/03/1973', 'age': 41}

print(account)

print('\n Display keys ')
print(account.keys())

print('\n Display value: ')
print(account.values())

account.update({'fname': 'Azad', 'lname': 'Abdulla', 
				'address': '206 Valence Road', 
				'date_of_birth': '18/01/1975', 'age': 39})

print(account)

del account['date_of_birth']

print(account)
print()
print(len(account))

print('\n Display items:')
print(account.items())

print('#######################\n')
print(dir(account))
"""
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
'__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 
'popitem', 'setdefault', 'update', 'values']
"""