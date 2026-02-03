import datetime


now = datetime.datetime.today()
print('\n\t Today now: ', now)

print('')

yet = datetime.datetime.now()
print('\n\t Today now: ', yet)
print('\n\t Total micro second: ', yet.microsecond)

# Convert strings to datetimes
'''
Module: datetime
Class: datetime
Method: strptime()
'''
date_of_birth = '28/03/1973'
my_brithday = datetime.datetime.strptime(date_of_birth, '%d/%m/%Y')
print('')
print('\n\t My Birthday: ', my_brithday)

print('\n\t Type: ', type(my_brithday))
