import csv

output = ''

# create an empty list to put the data here
names = []


# this is not completed
with open('csv/details.csv', 'r') as csv_data:
    csv_rd = csv.reader(csv_data)

    print('\n\t next:', next(csv_rd))
    print('\n\t next:', next(csv_rd))

    print('#' * 70)
    for line in csv_rd:
        if line[1] == 'No Reward':
            break
                    # fname     lname       postcode
        names.append(f'{line[0]} {line[1]} {line[2]}')

html_data = f"<p> Total of data are {len(names)} in this csv file. Thanks.</p>"

# print('\n\t ', html_data)


html_data += '\n<ul>'

for name in names:
    html_data += f'\n\t<li>{name}</li>'

html_data += '\n</ul>'

print('\n\t ', html_data)