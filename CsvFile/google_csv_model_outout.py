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

csvfile = open('google_stock_data.csv', newline='')
reader = csv.reader(csvfile)

# we read the header first
header = next(reader)

print(' We need to find a solution how to saperate date float and int in the body')


print(50 * '##')
# create empty list
data = []

for row in reader:
    # row = [Date, open, high, low, close, volum, adj. close]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])  # open alone is a function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    # now we add all to the empty list created before the for loop
    data.append([date, open_price, high, low, close, volume, adj_close])

    # data.save()
print(data[0])

# stored data daily
new_file = ('google_output.csv')

file = open(new_file, 'w')
writer = csv.writer(file)
writer.writerow(['Date', 'Return'])

for x in range(len(data) - 1):
    today_row = data[x]
    today_date = today_row[0]
    today_price = today_row[-1]
    yesterday_row = data[x + 1]
    yesterday_price = yesterday_row[-1]

    daily_return = (today_price - yesterday_price) / yesterday_price
    formatted_date = today_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, '\t\t', daily_return])
