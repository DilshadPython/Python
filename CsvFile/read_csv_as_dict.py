import csv

'''
	to separate value by using a field in csv file use delilmiter by ,
'''
names = []
with open('csv/details.csv', 'r') as csvfile:
    data_csv = csv.DictReader(csvfile)

    for line in data_csv:
        if line['first_name'] == 'No Reward':
            break
        # to read the index in one line use following
        names.append(f'{line['first_name']} {line["last_name"]}')
        # print(line)

for name in names:
    # we display only the 3 details in each line
    print('\n\t Name: ', name)