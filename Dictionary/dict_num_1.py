'''
Dictionaries in python are mapping, the mapping is collection of objects are sorted by key
'''


text = {}


print(text)
print('##########################################', '\n')

print(' Building dictionary')
text['num'] = 22
text['num1'] = 47
text['num2'] = 10
text['num3'] = 84
text['num4'] = 65
print(text)

print('\n')
print('##########################################')
print(' Select only by KEYS      ')
print('##########################################', '\n')

print(text.keys())

print('\n')
print('##########################################')
print(' Select only by VALUES                 ')
print(text.values())


print('\n')
print('##########################################')
print(' Changed it to Tuple')
print('\n')
print(text.items())