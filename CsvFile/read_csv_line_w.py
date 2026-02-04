import csv

'''
	to separate value by using a field in csv file use delimiter by ,

'''

with open('csv/property-data.csv', 'rt') as csvfile:
    spamreader = csv.reader(csvfile)

    # we rewrite the file to the new csv file separate via #
    with open('created/new_file.csv', 'w') as new_csv_file:
        csv_file_writer = csv.writer(new_csv_file, delimiter='\t')

        for row in spamreader:
            csv_file_writer.writerow(row)
