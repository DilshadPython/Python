'''
Dictionaries in python are mapping, the mapping is collection of objects are sorted by key
'''

defin_dict = {'key': 'value'}

details = {'name': 'Dilshad', 'last_name': 'Abdulla', 'age': 44,
           'languages': ['English', 'German', 'Kurdish', 'Arabic']}

details['email'] = 'dilshad.abdulla@gmail.com'

print(details['name'])
print(details['last_name'])
print(details['age'])

print('\n#####################')
print(details['last_name'][0])
print(details['last_name'][1:])
print
print(details['last_name'][:2])
print(details['last_name'][::-1])

print('\n#####################')
print(details['name'].upper())

print('\n#####################')
print(details['languages'])

print('\n#####################')
print(details.get('addrees'), ' <<< yes that is correct there is no address')

print('\n#####################')
print(details.get('email', ' Not Found'))
print(details.get('website', ' Not Found'))

print('\n#####################')
print(details)
