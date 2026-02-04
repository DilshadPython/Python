import csv

# we need to add the import datetime after come to line 38
from datetime import datetime

'''
We use csv model because we have sometime long text include ' '
'''
print(dir(csv))
'''
['Dialect', 'DictReader', 'DictWriter', 'Error', 'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONE', 
'QUOTE_NONNUMERIC', 'Sniffer', 'StringIO', '_Dialect', '__all__', '__builtins__', '__cached__', 
'__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'excel', 
'excel_tab', 'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'register_dialect', 
'unix_dialect', 'unregister_dialect', 'writer']
'''
# We will use excel function read and write

csvfile = open('csv/google_stock_data.csv', newline='')
reader = csv.reader(csvfile)

# we read the header first
header = next(reader)

# read the body
body = [row for row in reader]

print(header)
print(50 * '==')
print(body[0])
