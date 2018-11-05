create_dict = dict()  # or create_dict = {}

# add the keys and values to the dictionary
create_dict['Hello'] = 219
create_dict['Hi'] = 90
create_dict['Hey'] = 1
create_dict['Merci'] = 87

print(create_dict)

print('\n')
print('Display the keys')
print(create_dict.keys())

print('\n')
print('Display the values')
print(create_dict.values())


print('\n')
print('Display keys and values as a Tuple')
print(create_dict.items())

print('\n')
print('Create dictionary from the above keys and values using for loops')
for x in create_dict:
    new_dict = '%s %d' % (x, create_dict[x])
    print(new_dict)

print('\n')
print('')
for index, value in enumerate(create_dict):
    print(index, value, create_dict[value])
