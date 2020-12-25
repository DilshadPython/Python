import time
import datetime

today = datetime.date.today()

'''
weekday shows Monday 0 Sunday 6
isoweekday shows Monday 1 Sunday 7
'''
print(today)
print(today.weekday(), ' = Weekday')
print(today.isoweekday(), ' = Isoweekday')
