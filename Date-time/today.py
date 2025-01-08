import datetime


now = datetime.datetime.today()
print(now)

print('')

yet = datetime.datetime.now()
print(yet)
print(yet.microsecond)

# Convert strings to datetimes
'''
Module: datetime
Class: datetime
Method: strptime()
'''
datebirth = '28/03/1973'
mybrithday = datetime.datetime.strptime(datebirth, '%d/%m/%Y')
print('')
print('My Birthday: ', mybrithday)

print(type(mybrithday))
