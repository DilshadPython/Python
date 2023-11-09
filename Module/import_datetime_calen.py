import datetime
import calendar

today_is = datetime.date.today()

print('\n Today is: ', today_is)

print(calendar.isleap(2015))
print(calendar.isleap(2020))
print(calendar.isleap(2035))
