import sys

ages = {
    'adam': 33,
    'tom': 21,
    'claudia': 28,
    'sam': 37,
    'george': 25
}

key = str(input('Enter a name: '))

try:
    print('We are checking the key of dict by asking enter the name.')
    print('The value of {0} is the age: {1}'.format(key, ages[key]))
except KeyError:
    print('Trapped error')
    print('The key you have enetered (', key, ') does not exisit' )
    print('====== End of script don\'t display last print ======')
    sys.exit() 
print('Program continue ...')


