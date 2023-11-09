'''
How strip works with removeprefix and the different
'''

myword = 'afterbreakfast'
yourword = 'Hbeforebreakfast'


print('Testing strip with after:')
print(myword.strip('after'))
print('\nTesting strip with before:')
print(myword.strip('before'))

print;print;

print('\nTesting remove with before:')
print(yourword.removeprefix('before'))
print(yourword.removeprefix('before'))


# print('Testing strip:')
# print(myword.strip('afterb'))

# print('\nTesting remove:')
# print(myword.removep('afterb'))