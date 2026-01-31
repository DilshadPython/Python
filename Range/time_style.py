import datetime

today = datetime.datetime(2026, 1, 30, 3, 20, 33)
print('I wrote this code ', today)

print()
style_date = 'I wrote this code {:%B %d, %Y, %H:%M:%S}'.format(today)
print(style_date)

print()
style_date = 'I wrote this code {0:%B %d, %Y, %H:%M:%S} on {0:%A} day of the year {0:%j}'.format(today)
print(style_date)
