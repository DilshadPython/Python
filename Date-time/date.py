import datetime

print(dir(datetime))

# output
'''
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__', '_divide_and_round', 
'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo'
'''
# class Date(builtins.object):
# 	date(year, month, day)
#
dilmac = datetime.date(1973, 3, 28)
print(dilmac)

print('')
today = datetime.datetime.now()

print(today)

print('')
date_example = datetime.date(2010, 2, 15)

# to add 76 days to the date example
dt = datetime.timedelta(76)
print(date_example + dt)

print('')

dt = datetime.timedelta(-176)
print(date_example + dt)