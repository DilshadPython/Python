import csv

'''
	to saperate value by using a field in csv file use delilmiter by ,

'''

with open('property-data.csv', 'rt') as csvfile:
    spamreader = csv.reader(csvfile)
    # next read the 0 index first which is Address on index 6 but not printed
    # out jump to next line
    next(spamreader)
    for row in spamreader:
        # to read the index in one line use following
        # print(row[1])
        print(row[5])
