'''
Dictionaries in python are mapping, the mapping is collection of objects are sorted by key
'''

defin_dict = {'key': 'value'}

text = {'name': 'Dilshad', 'last_name': 'Abdulla', 'age': 44}

print(text['name'])
print(text['last_name'])
print(text['age'])

print('#####################')
print(text['last_name'][0])
print(text['last_name'][1:])
print
print(text['last_name'][:2])
print(text['last_name'][::-1])

print('#####################')
print(text['name'].upper())