import csv

'''
	to separate value by using a field in csv file use delimiter by ,

'''

with open('csv/property-data.csv', 'r') as csvfile:
    csv_file_to_read = csv.DictReader(csvfile)

    with open('created/new_csv_to_write.csv', 'w') as csv_to_write:
        fieldnames = [
            'PROPERTY_REFERENCE',
            'PRICE',
            'BEDROOMS',
            'BATHROOMS',
            'HOUSE_NUMBER',
            'ADDRESS',
            'REGION',
            'POSTCODE',
            'PROPERTY_TYPE'
        ]

        csv_writer = csv.DictWriter(
            csv_to_write, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for field in csv_file_to_read:
            csv_writer.writerow(field)
