month_table = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
}

print(month_table.keys())
print(month_table.values())
print('\n')

month_table.pop('Mar')

print(month_table.keys())
print(month_table.values())