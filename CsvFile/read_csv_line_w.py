import csv

'''
	to separate value by using a field in csv file use delimiter by ,
'''

with open('csv/property_data.csv', 'rt') as csvfile:
    spamreader = csv.reader(csvfile)

    # we rewrite the file to the new csv file separate via #
    with open('created/new_file.csv', 'w') as new_csv_file:
        # fieldheader = ['PROPERTY_REFERENCE', 'PRICE', 'BEDROOMS', 'BATHROOMS', 'HOUSE_NUMBER', 'ADDRESS',
        #                'REGION', 'POSTCODE', 'PROPERTY_TYPE']
        # csv_file_writer= csv.DictWriter(new_csv_file, fieldheader=fieldheader, delimiter='\t')
        # csv_file_writer.writeheader()

        csv_file_writer = csv.writer(new_csv_file, delimiter='\t')

        for row in spamreader:
            csv_file_writer.writerow(row)

# now we read the new csv file we created
with open('created/new_file.csv', 'r') as new_file:
    read_csv = csv.reader(new_file, delimiter='\t')
    print('\n ######')
    for row in read_csv:
        print(row)
