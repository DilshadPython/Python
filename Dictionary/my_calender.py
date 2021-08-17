month_table = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'Decmber'
}

print('This month is >> ', month_table.get('Aug'))
print('\n')

for k in month_table:
	print(month_table[k])

print('\n')

for x in month_table.values():
	print(x)

print('\n')

for x in month_table.keys():
	print(x)