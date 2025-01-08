import csv

'''
	to saperate value by using a field in csv file use delilmiter by ,

'''

with open('property-data.csv', 'r') as csvfile:
    spamreader = csv.DictReader(csvfile)

    for row in spamreader:
        # to read the index in one line use following
        print(row)
