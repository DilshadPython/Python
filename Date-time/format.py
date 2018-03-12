# https://docs.python.org/3/library/datetime.html
'''
%A weekday full name
%B month full name
%d the day of the month
%Y year
'''
import datetime


dilmac = datetime.date(1973, 3, 28)

day_format = dilmac.strftime("%A, %B %d, %Y")

print(day_format)

mybith = 'I am born in Kurdistan in the {:%A, %B %d, %Y}.'

print('My name is Dilshad and ' + mybith.format(dilmac))

print('')
launch_date = datetime.date(1973, 3, 28)
launch_time = datetime.time(20, 16, 2)
launch_datetime = datetime.datetime(1973, 3, 28, 20, 16, 2)

print(launch_date)
print(launch_time)
print(launch_datetime)

print('')

print(launch_time.hour, launch_time.minute, launch_time.second)
print('')

print(launch_datetime.year, launch_datetime.month, launch_datetime.day)

