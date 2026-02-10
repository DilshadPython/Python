import csv

output = ''

# create an empty list to put the data here
names = []
emails = []

# this is not completed
with open('csv/details.csv', 'r') as csv_data:
    csv_rd = csv.reader(csv_data)

    # print('\n\t next:', next(csv_rd))
    # print('\n\t next:', next(csv_rd))

    print('#' * 70)
    for line in csv_rd:
        if line[1] == 'No Reward':
            break
                    # fname     lname       postcode
        names.append(f'{line[0]} {line[1]} {line[2]}')



# display first and last name
for name in names:
    # we display only the 3 details in each line
    print('\n\t Name: ', name)

# this is not completed
with open('csv/details.csv', 'r') as mail_in_csv:
    csv_mail = csv.reader(mail_in_csv)

    print('#' * 70)
    for line in csv_mail:
        emails.append(f'{line[3]}')

# display first and last name
for mail in emails:
    # we display only the 3 details in each line
    print('\n\t Emails: ', mail)