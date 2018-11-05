import csv

'''
	to saperate value by using a field in csv file use delilmiter by ,

'''

with open('created/new_file.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')

    for row in spamreader:
        # to read the index in one line use following
        print(row)
