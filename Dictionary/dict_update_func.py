
details = {'name': 'Dilshad', 'last_name': 'Abdulla', 'age': 44,
           'languages': ['English', 'German', 'Kurdish', 'Arabic']}

print('\n', details)

details.update({'email': 'dilshad.abdulla@gmail.com', 'age': 45,
                'website': 'https://dilshadabdulla.net'})

print('\n Update the dictionary details. \n')
print(details)

del details['website']
print('\n', details)

print('\n - Collect all keys in the dictionary. \n')
print(len(details))

print('\n - Display only the keys: \n')
print(details.keys())

print('\n - Display the value only: \n')
print(details.values())

print('\n - Display both keys and values together: \n')
print(details.items())

print('\n - Display another way yje key and the value: \n')
for key, value in enumerate(details.items()):
    print(key, value)
